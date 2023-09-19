from decouple import config
from casino import Roulette

my_money = config('MY_MONEY', default=0, cast=int)
print(f'You started with {my_money}')
roulette = Roulette()
while True:
    print('All right, gents, place your bets')
    slot = int(input('Choose 1 slot from 1 to 30: '))
    bet = int(input(f'Your bet: '))

    if roulette.is_not_valid_slot(slot):
        print(f'Choose write slot in range {roulette.slots}')
        continue

    winning_number = roulette.round()
    if winning_number > my_money:
        print(f'Your balance is {my_money}')
        continue

    if slot == winning_number:
        prize = bet ** 2
        my_money += prize
        print(f'Congratulation! You won: {prize}')
    else:
        my_money -= bet
        print(f'Unfortunately, you lose yor bet')

    print(f'Your balance is {my_money}')

    try_again = input('Do you want try again? Default is y [y/n]: ')
    if not try_again:
        try_again = 'y'
    if try_again != 'y':
        break

print(f'Your total balance is {my_money}')
