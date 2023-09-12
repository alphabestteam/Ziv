from product import Product


class Customer:
    def __init__(self, customer_name: str) -> object:
        """
        Initializes Costumer product
        """
        self.customer_name = customer_name
        self.product_list = []

    def product_index(
        self,
        product_name: str,
    ) -> int:
        """
        Receives name of product
        Searches customer's product list for said product
        If the function finds the product, returns its index, otherwise returns -1
        """
        for current_item in range(len(self.product_list)):
            if self.product_list[current_item]["Product"].product_name == product_name:
                return current_item
        return None

    def add_product(self, product_name: str, product_units: int) -> None:
        """
        The function checks if the product is already in the cart, the function adds to the amount
        Otherwise, the function adds the new product
        """
        in_cart = self.product_index(product_name)
        if in_cart is None:
            self.product_list.append(
                {"Product": Product(product_name), "Amount": product_units}
            )
        else:
            self.product_list[in_cart]["Amount"] += product_units
        print("Your product was successfully added!")

    def remove_product(self, product_name: str, product_units: int) -> None:
        """
        The function removes the units of the product from the list
        """
        in_cart = self.product_index(product_name)
        self.product_list[in_cart]["Amount"] -= product_units
        print("Your product was successfully removed!")

    def calc_customer(self) -> int:
        """
        The function prints that total shopping sum of the customer
        """
        shopping_balance = 0
        for current_item in self.product_list:
            shopping_balance += current_item["Product"].calc_product(
                current_item["Amount"]
            )
        return shopping_balance

    def print_list(self) -> None:
        """
        Iterates over list of dictionaries and prints relevant info
        """
        for current_item in self.product_list:
            current_item["Product"].to_str(current_item["Amount"])
