from collections import OrderedDict
from random import randint

languages = OrderedDict()
languages['as'] = 'py'
languages['sa'] = 'c'
for name, language in languages.items():
    print(name.title() + "'s language is " + language + ".")


class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
die=Die(10)
die.roll_die()