class People:
    def __init__(self):
        """
        Initializes people object
        """
        self.people_list = []


    def add_person(self, input_name: str) -> None:
        """
        the function receives a person's name
        The function adds the name to the people_list attribute
        """
        self.people_list.append(input_name)


    def __iter__(self):
        """
        The function makes the object iterable
        """
        return iter(self.people_list)

people_obj = People()
people_obj.add_person("Patrick")
people_obj.add_person("Starr")
for current_person in people_obj:
    print(current_person)
