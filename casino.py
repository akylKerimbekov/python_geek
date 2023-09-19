from random import choice
from decouple import config


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


class Board:
    def __init__(self):
        self.__roulette = Roulette()

    def validate_slot(self, slot):
        return slot in self.__roulette

    def get_slots(self):
        return self.__roulette.slots

    def receive_bet(self, slot):
        winning_number = self.__roulette.round()
        return slot == winning_number


class Croupier:
    @staticmethod
    def greeting():
        print(config('GREETING'))

    @staticmethod
    def is_not_valid_bet(bet, money):
        if bet > money:
            print(f"{config('YOUR_BALANCE')} {money}")
            return True

        return False

    @staticmethod
    def is_not_valid_slot(slot, slots):
        if slot not in slots:
            print(f"{config('CHOOSE_RIGHT_SLOT')} {slots}")
            return True

        return False

    @staticmethod
    def round_roulette(slot, board):
        return board.receive_bet(slot)

    @staticmethod
    def on_success(bet):
        prize = bet ** 2
        print(f"{config('CONGRATS')} {prize}")
        return prize

    @staticmethod
    def on_failure(bet):
        print(f"{config('FAIL')}")
        return bet

    @staticmethod
    def balance_inform(money):
        print(f'Your balance is {money}')

    @staticmethod
    def exit_round():
        try_again = input('Do you want to exit? Default is y [y/n]: ')
        if not try_again or try_again == 'y':
            return True
        return False
