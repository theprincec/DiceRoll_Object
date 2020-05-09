from random import randint

class DiceRoll(object):
    def __init__(self, object):
        self.dice_name = object
        self.min_roll = 1
        self.max_roll = 6

    def random_roll(self):
        return randint(self.min_roll, self.max_roll)

# TheMan = DiceRoll('TheMan')
# print(TheMan.__dict__)
# print(TheMan.random_roll())



# print(total)
# name = input('what is your name?')

# status = input(f'hi {name} thanks for playing')
