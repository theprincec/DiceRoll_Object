from helpers import *

name = input('what is your name?')
# status = input(f'hi {name} thanks for playing')

dice1 = DiceRoll('dice1')
dice2 = DiceRoll('dice2')

game_status = input(f'{name}, Press a key to roll the dice')
while game_status is not 'q':
    total_roll = dice1.random_roll() + dice2.random_roll()
    print(total_roll)
    game_status = input(f"{name}, Press any key to roll the dice. Press 'q' to quit")
# print(f'{name} press a key to play.')
# print(name)
# print(total_roll)


# if user == 'chris':
#     print('truee')
