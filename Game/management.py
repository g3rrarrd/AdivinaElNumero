from Game import number as n

class management:

    def __init__(self):
        self.__number = None
        self.__tries = 0

    def generate_number(self):
        numero = n.number()
        self.__number = numero.number_generate()

    def play(self, number_player):
        if number_player == self.__number:
            self.__tries += 1
            print("Enhorabuena")
            print("Numero de intentos: %d" % self.__tries)
            return True
        self.__tries += 1
        return False

    def get_number(self):
        return self.__number
        