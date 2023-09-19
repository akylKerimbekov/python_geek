from random import choice
from decouple import config


class Roulette:
    def __init__(self):
        self.__slots = tuple(range(1, 31))

    @property
    def slots(self):
        return self.__slots

    def spin(self):
        return choice(self.__slots)


class Board:
    def __init__(self):
        self.__roulette = Roulette()

    def is_valid_slot(self, slot):
        return slot in self.__roulette.slots

    def spin_roulette(self):
        return self.__roulette.spin()


class Croupier:
    @staticmethod
    def greet():
        print(config('GREETING'))

    def is_valid_bet(bet, balance):
        if bet > balance:
            print(f"{config('YOUR_BALANCE')} {balance}")
            return False
        return True

    @staticmethod
    def is_bet_winning(slot, board):
        return slot == board.spin_roulette()

    @staticmethod
    def handle_win(bet):
        prize = bet ** 2
        print(f"{config('CONGRATS')} {prize}")
        return prize

    @staticmethod
    def handle_loss(bet):
        print(f"{config('FAIL')}")
        return bet

    @staticmethod
    def inform_balance(money):
        print(f'Your balance is {money}')

    @staticmethod
    def should_exit():
        try_again = input('Do you want to exit? Default is y [y/n]: ')
        return not try_again or try_again == 'y'
