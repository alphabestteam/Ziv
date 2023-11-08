/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/


document.addEventListener('DOMContentLoaded', function () {
  function getMenu() {
    return new Promise((resolve, reject) => {
      fetch('http://localhost:8000/menu')
        .then(getRequest => {
          if (!getRequest.ok) {
            reject(new Error(`Error fetching menu: ${getRequest.status}`));
            return;
          }

          getRequest.json()
            .then(menuData => {
              resolve(menuData);
            })
            .catch(error => {
              reject(new Error(`Error parsing JSON getRequest: ${error.message}`));
            });
        })
        .catch(error => {
          reject(new Error(`Error fetching user data: ${error.message}`));
        });
    });
  }
  getMenu()
    .then(menuData => {
      addMenu(menuData);
      orderSummaryHandler();
      const lastOrderButton = document.getElementById("get-last-order-button");
      lastOrderButton.addEventListener("click", getLastOrder);
      const submitButton = document.getElementById("submit-button");
      submitButton.addEventListener("click", submitOrder);
    })
    .catch(error => {
      console.error('Error fetching menu:', error);
    });

});

function addMenu(menuData) {
  const iterableMenu = menuData["items"];
  const menu = document.getElementById("menu");

  for (const key in iterableMenu) {
    const item = document.createElement('div');
    item.setAttribute('class', 'menuItems');
    // Matches the colors of the blocks on the website
    const style = "background-color: #434242";
    item.setAttribute("style", style);
    const itemName = document.createElement('h1');
    // Format price based on US currency
    const formattedPrice = new Intl.NumberFormat('en-US', {
      maximumSignificantDigits: 3, style: 'currency',
      currency: 'USD',
    }).format(iterableMenu[key]["price"]);
    itemName.innerHTML = iterableMenu[key]["name"].concat("  ", formattedPrice);
    const itemDescription = document.createElement('p');
    itemDescription.innerHTML = iterableMenu[key]["description"];

    const itemPriceQuantity = document.createElement('input');
    itemPriceQuantity.setAttribute('id', 'quantity-' + iterableMenu[key]["name"]);
    itemPriceQuantity.setAttribute('type', 'number');
    itemPriceQuantity.setAttribute('min', '0');
    itemPriceQuantity.setAttribute('max', '5');
    itemPriceQuantity.setAttribute('placeholder', '0');

    item.appendChild(itemName);
    item.appendChild(itemDescription);
    item.appendChild(itemPriceQuantity);
    menu.appendChild(item);
  }
}



function orderSummaryHandler() {
  const allItems = document.querySelectorAll(".menuItems");
  const summaryElement = document.querySelector('#order-summary');

  const itemSummary = {}; // Object to track item quantities in the order

  allItems.forEach(currentItem => {
    let itemTitle = currentItem.querySelector('h1').textContent;
    const priceAndName = itemTitle.split("  ");
    itemTitle = priceAndName[0];
    const itemPrice = parseFloat(priceAndName[1].replace('$', '')); // Convert price to a number
    const itemQuantityInput = currentItem.querySelector('input');

    // Whenever the input field changes
    itemQuantityInput.addEventListener('change', () => {
      const itemQuantity = parseInt(itemQuantityInput.value);

      if (itemQuantity >= 0 && itemQuantity <= 5) {
        itemSummary[itemTitle] = {
          quantity: itemQuantity,
          price: itemPrice,
        };

        // Update the summary
        updateOrderSummary(itemSummary, summaryElement);
      } else {
        // Remove the item from the summary
        delete itemSummary[itemTitle];
        updateOrderSummary(itemSummary, summaryElement);
      }
    });
  });
}

function updateOrderSummary(itemSummary, summaryElement) {
  // Clear the existing summary, by default
  summaryElement.innerHTML = '<h3>Current Order Summary:</h3>';

  let isEmptyFlag = true; // Flag to check if the order is empty

  for (const itemTitle in itemSummary) {
    const { quantity, price } = itemSummary[itemTitle];

    if (quantity > 0) {
      const itemTotalPrice = quantity * price;
      const summaryItemText = `${itemTitle} (${quantity} x $${price.toFixed(2)} = $${itemTotalPrice.toFixed(2)})`;
      summaryElement.insertAdjacentHTML('beforeend', `<p>${summaryItemText}</p>`);
      isEmptyFlag = false; // At least one item in the order
    }
  }

  // If the order is empty, display "Empty Order"
  if (isEmptyFlag) {
    summaryElement.insertAdjacentHTML('beforeend', '<p>Empty Order</p>');
  }
}


function getLastOrder() {
  async function fetchOrderData() {
    try {
      const getRequest = await fetch('http://localhost:8000/latest-order');
      if (!getRequest.ok) {
        throw new Error(`Error fetching the last order: ${getRequest.status}`);
      }

      const orderData = await getRequest.json();

      const displayedOrder = document.getElementById('order_details');
      displayedOrder.textContent = organizeExtractedOrder(orderData["items"]);
    } catch (error) {
      console.error('Error fetching the last order:', error);
    }
  }

  (async () => {
    await fetchOrderData();
  })();
}

function organizeExtractedOrder(orderList) {
  let orderDescription = "Last Order: ";
  for (let item of orderList) {
    orderDescription += `${item["name"]}: Quantity- ${item["quantity"]} Price- ${item["price"]}\n`;
  }
  return orderDescription;
}

function submitOrder() {
  const itemSummary = getItemSummary(); // Get the item summary from the order
  const orderData = { items: [] };

  for (const itemTitle in itemSummary) {
    const { quantity, price } = itemSummary[itemTitle];
    if (quantity > 0) {
      orderData.items.push({
        name: itemTitle,
        quantity: quantity,
        price: price,
      });
    }
  }

  // Check if there are items in the order
  if (orderData.items.length === 0) {
    console.log('No items in the order to submit.');
    return;
  }

  fetch('http://localhost:8000/orders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(orderData),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error(`Error submitting order: ${response.status}`);
      }
      // Handle success or errors
    })
    .catch(error => {
      console.error(`Error submitting order: ${error.message}`);
    });
}

function getItemSummary() {
  const allItems = document.querySelectorAll(".menuItems");
  const itemSummary = {};

  allItems.forEach(currentItem => {
    let itemTitle = currentItem.querySelector('h1').textContent;
    const priceAndName = itemTitle.split("  ");
    itemTitle = priceAndName[0];
    const itemPrice = parseFloat(priceAndName[1].replace('$', '')); //Turn title back to number
    const itemQuantityInput = currentItem.querySelector('input');
    const itemQuantity = parseInt(itemQuantityInput.value);

    itemSummary[itemTitle] = {
      quantity: itemQuantity,
      price: itemPrice,
    };
  });

  return itemSummary;
}