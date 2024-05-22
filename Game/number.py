import random as r

class number:

    def __init__(self):
        self.__number = None

    def number_generate(self):
        self.__number = r.randint(1,50)
        return self.__number