class Backpack:
    """A class representing a backpack with a name, color, and maximum size.

    Attributes:
        name (str): The name of the backpack.
        color (str): The color of the backpack.
        max_size (int): The maximum number of items the backpack can hold (default is 5).
        contents (list): A list to store the items in the backpack.
    """

    def __init__(self, name, color, max_size=5):
        """Initializes a new instance of the Backpack class.

        Parameters:
            name (str): The name of the backpack.
            color (str): The color of the backpack.
            max_size (int, optional): The maximum number of contents the backpack can hold (default is 5).
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Adds an item to the backpack's contents if there is room.

        Parameters:
            item: The item to be added to the backpack.

        Returns:
            None

        Prints "No Room!" if the backpack is at its maximum capacity.
        """
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def dump(self):
        """
        Removes all items from the backpack.

        Returns:
            None
        """
        self.contents = []


def test_backpack():
    testpack = Backpack("Barry", "black")
    if testpack.name != "Barry":
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)
    print("Contents:", testpack.contents)


test_backpack()
