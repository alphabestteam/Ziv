from customer import Customer


class Register:
    def __init__(self):
        self.profits = 0
        self.sales_list = []

    def checkout_customer(self, new_customer: Customer) -> None:
        """
        Adds new customer object to sales_list attribute of register
        """
        self.sales_list.append(new_customer)
        self.profits += new_customer.calc_customer()

    def print_summary(self) -> None:
        """
        Prints the profits of the register
        Iterates over the customer list and prints all customers
        """
        print(
            f"This register made a total of {self.profits}. Here is the detailed shopping list:"
        )
        for item in self.sales_list:
            print(f"Customer name: {item.customer_name} Shopping list:\n")
            item.print_list()


def product_receiver():
    """
    Receives and validates the product's name and amount and returns them if they're valid
    """
    try:
        product_name, product_amount = input(
            "Enter the product's name and amount, separated by whitespaces: "
        ).split(" ")
        if int(product_amount) > 0:
            return product_name, int(product_amount)
        else:
            print("The amount can't be negative")
            return None
    except TypeError:
        print("One of the inputs doesn't make sense")
        return None


def choice_manager() -> int:
    """
    Receives and validates user's action choice and returns it if ir's valid
    """
    selected_choice = input(
        "Please select an action(To add a product: 1, To remove a product: 2, For checkout: 3): "
    )
    if selected_choice not in ["1", "2", "3"]:
        print("Invalid action!")
        return -1
    else:
        return int(selected_choice)
