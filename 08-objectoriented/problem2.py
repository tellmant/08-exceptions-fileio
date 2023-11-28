from problem1 import Backpack


class Jetpack(Backpack):
    """
    A class representing a jetpack, a specialized type of backpack with additional features.

    Attributes:
        name (str): The name of the jetpack.
        color (str): The color of the jetpack.
        max_size (int): The maximum number of items the jetpack can hold (default is 2).
        fuel (int): The amount of fuel in the jetpack (default is 10).

    Methods:
        __init__(self, name, color, max_size=2, fuel=10):


        fly(self, fuel):
            Attempts to fly the jetpack using the specified amount of fuel.

            Parameters:
                fuel (int): The amount of fuel to be used for flying.

            Returns:
                None

            Prints "Not enough fuel!" if there is insufficient fuel.

        dump(self):
            Removes all items from the jetpack and sets the fuel level to zero.

            Returns:
                None
    """

    def __init__(self, name, color, max_size=2, fuel=10):
        """Initializes a new instance of the Jetpack class.

        Parameters:
            name (str): The name of the jetpack.
            color (str): The color of the jetpack.
            max_size (int, optional): The maximum number of items the jetpack can hold (default is 2).
            fuel (int, optional): The amount of fuel in the jetpack (default is 10).
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, fuel):
        """Attempts to fly the jetpack using the specified amount of fuel.
        Prints "Not enough fuel!" if there is insufficient fuel.

        Parameters:
            fuel (int): The amount of fuel to be used for flying.

        Returns:
           None
        """
        if fuel > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= fuel

    def dump(self):
        """Removes all items from the jetpack and sets the fuel level to zero.

        Returns:
            None
        """
        Backpack.dump(self)
        self.fuel = 0
