import random


class Person:
    names_list = [
        "Ziv",
        "Jordan",
        "Maya",
        "Coral",
        "Bob",
        "Sponge",
        "Patrick",
        "Gary",
        "Mrs. Puff",
    ]

    def __init__(self) -> object:
        """
        Object constructor, creates Person
        """
        self.name = Person.names_list[random.randint(0, len(Person.names_list) - 1)]
        self.age = random.randint(0, 100)
        self.id = Person.create_id()

    @staticmethod
    def create_id() -> int:
        """
        The function runs nine times and randomly selects a digit
        The function adds the digit and creates a string id
        The function returns the is as an integer
        """
        generated_id = ""
        for _ in range(9):
            generated_id += str(random.randint(0, 9))
        return int(generated_id)

    def print_properties(self):
        """
        Prints all the properties of the object
        """
        print(f"Name: {self.name}\nAge: {self.age}\nID: {self.id}")

    def get_name(self) -> str:
        """
        Returns object's name property
        """
        return self.name

    def set_name(self, new_name: str) -> None:
        """
        Receives new name and changes the object's name property
        """
        self.name = new_name

    def get_age(self) -> int:
        """
        Returns object's age property
        """
        return self.age

    def set_name(self, new_age: int) -> None:
        """
        Receives new age and changes the object's name property
        """
        self.name = new_age

    def get_id(self) -> int:
        """
        Returns object's id property
        """
        return self.id

    def set_name(self, new_id: int) -> None:
        """
        Receives new id and changes the object's name property
        """
        self.name = new_id
