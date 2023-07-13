"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 8. '''

class Animal:
    def speak(self):
        print('A sound')
    def reply(self):
        self.speak()
class Mammal(Animal):
    def speak(self):
        print('Mmm')
class Cat(Mammal):
    def speak(self):
        print('Meow')
class Dog(Mammal):
    def speak(self):
        print('Bark')
class Primate(Mammal):
    def speak(self):
        print('Hello, world')
class Hacker(Primate):
    pass
