from helpers import *

name = input('what is your name?')
# status = input(f'hi {name} thanks for playing')

dice1 = DiceRoll('dice1')
dice2 = DiceRoll('dice2')

game_status = input(f'{name}, Press a key to roll the dice')
while game_status is not 'q':
    total_roll = dice1.random_roll() + dice2.random_roll()
    # total_roll = 11
    print(total_roll)
    if total_roll == 11:
        print(f"SNAKE EYES. You're a winner, {name}!")
    elif (total_roll == 2) or (total_roll == 3) or (total_roll == 12) :
        print('Craps!')
    else:
        pass
    game_status = input(f"{name}, Press any key to roll the dice. Press 'q' to quit")
# print(f'{name} press a key to play.')
# print(name)
# print(total_roll)


# if user == 'chris':
#     print('truee')
