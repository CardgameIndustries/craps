#!/usr/bin/env python
import random

class die:
    """A multi sided die"""
    def __init__(self, number_of_sides):
        self.sides = number_of_sides

    def roll(self):
        return random.randint(1,self.sides)

# sixer = die(6)
# print(sixer.roll())

