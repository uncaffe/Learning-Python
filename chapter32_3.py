"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 3. '''

from chapter32_2 import MyList

class MyListSub(MyList):
    calls = 0
    
    def __init__(self, start):
        self.calls = 0
        self.adds = 0
        self.muls = 0
        MyList.__init__(self, start)

    def __add__(self, other):
        print('add: ' + str(other))
        MyListSub.calls += 1
        self.calls += 1
        self.adds += 1
        return MyList.__add__(self, other)

    def __radd__(self, other):
        print('radd: ' + str(other))
        MyListSub.calls += 1
        self.calls += 1
        self.adds += 1
        return MyList.__radd__(self, other)

    def __mul__(self, other):
        print('mul: ' + str(other))
        MyListSub.calls += 1
        self.calls += 1
        self.muls += 1
        return MyList.__mul__(self, other)

    def stats(self):
        return '''\n class calls: %s,
instamce calls: %s,
instance adds: %s,
instance muls: %s''' % (MyListSub.calls, self.calls, self.adds, self.muls)
    
if __name__ == '__main__':
    x = MyListSub('spam')
    y = MyListSub('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bar'])
    print(x.stats(), y.stats())

    print(['ham'] + y)
    print(x * 3)
    print(x.stats(), y.stats())
    
    
