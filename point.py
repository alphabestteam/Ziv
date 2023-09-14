class Point:
    def __init__(self, x_value: float, y_value: float):
        """
        Initializes Point object
        """
        self.x_value = x_value
        self.y_value = y_value

    def __eq__(self, external_point: object) -> bool:
        """
        Compares two objects of class Point
        Returns true if their x and y are the same, otherwise false
        """
        return (self.x_value == external_point.x_value) and (
            self.y_value == external_point.y_value
        )

    def __str__(self) -> str:
        """
        The function calls on the x and y attributes of the point
        the function converts to values to string and returns them
        """
        return str((self.x_value, self.y_value))

    def __add__(self, external_point: object):
        """
        Receives two point
        Adds their x values and y values
        Two numbers are returned
        """
        return Point(
            self.x_value + external_point.x_value, self.y_value + external_point.y_value
        )
