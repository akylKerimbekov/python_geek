from decouple import config
from casino import Board, Croupier

balance = config('MY_MONEY', default=0, cast=int)
print(f'You started with {balance}')

board = Board()
while True:
    Croupier.greet()

    try:
        slot = int(input('Choose 1 slot from 1 to 30: '))
        bet = int(input(f'Your bet: '))

        if not Croupier.is_valid_bet(bet, balance) or not board.is_valid_slot(slot):
            continue

        if Croupier.is_bet_winning(slot, board):
            balance += Croupier.handle_win(bet)
        else:
            balance -= Croupier.handle_loss(bet)

        Croupier.inform_balance(balance)

        if Croupier.should_exit():
            break
    except ValueError:
        continue

print(f"{config('YOUR_BALANCE')} {balance}")
