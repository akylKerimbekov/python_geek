from decouple import config

from casino import Board, Croupier

my_money = config('MY_MONEY', default=0, cast=int)
print(f'You started with {my_money}')

board = Board()
while True:
    Croupier.greeting()

    try:
        slot = int(input('Choose 1 slot from 1 to 30: '))
        bet = int(input(f'Your bet: '))

        if Croupier.is_not_valid_bet(bet, my_money) or Croupier.is_not_valid_slot(slot, board.get_slots()):
            continue

        if Croupier.round_roulette(slot, board):
            my_money += Croupier.on_success(bet)
        else:
            my_money -= Croupier.on_failure(bet)

        Croupier.balance_inform(my_money)

        if Croupier.exit_round():
            break
    except ValueError:
        continue

print(f"{config('YOUR_BALANCE')} {my_money}")
