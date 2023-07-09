"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 1. '''

class Adder:
    def __init__(self, start=[]):
        self.data = start
    def __add__(self, other):
        return ('Not implemented')

class ListAdder(Adder):
    def __add__(self, x):
        return self.data + x

class DictAdder(Adder): 
    def __add__(self, x):
        new = {}
        for k in self.data.keys(): new[k] = self.data[k]
        for k in x.keys(): new[k] = x[k]
        return new

class DictAdder2(Adder):
    def __init__(self, start={}):
        self.data = start    
    def __add__(self, x):
        y = self.data.copy()
        y.update(x)
        return y

if __name__ == '__main__':
    x = ListAdder([1, 2, 3])
    y = x + [4, 5, 6]
    print(y)

    z = DictAdder(dict(name = 'Robert')) + {'a': 1}
    print(z)
