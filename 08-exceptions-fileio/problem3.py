class ContentFilter:

    def __init__(self, filename):
        try:
            with open(filename, 'r') as f:
                self.file = filename
                self.content = f.readlines()

        except (FileNotFoundError, TypeError, OSError) as e:
            new_filename = input(" Please enter a valid file name: ")
            self.__init__(new_filename)


cf1 = ContentFilter("hello_world.txt")
cf2 = ContentFilter("not-a-file.txt")
cf3 = ContentFilter([1, 2, 3])
