from random import choice


class Roulette:
    def __init__(self):
        self.__slots = tuple(range(1, 31))

    @property
    def slots(self):
        return self.__slots

    def round(self):
        return choice(self.__slots)

    def is_not_valid_slot(self, slot):
        return not slot in self.__slots
