import random


class Product:
    def __init__(self, product_name: str):
        """
        Initialize product object
        """
        self.product_name = product_name
        self.product_price = random.randint(1, 20)

    def calc_product(self, product_units: int) -> int:
        """
        Returns the price of the product's total units
        """
        return product_units * self.product_price

    def to_str(self, product_units: int) -> None:
        """
        Prints the attributes of the object
        """
        print(
            f"{self.product_name}: Price-{self.product_price }  Units-{product_units}"
        )