"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 2. '''

class MyList:
    def __init__(self, start):
        self.wrapped = list(start)
        
    def __add__(self, other):
        return MyList(self.wrapped + other)
    
    def __mul__(self, time):
        return MyList(self.wrapped * time)

    def __radd__(self, other):
        return other + self.wrapped

    def __getitem__(self, offset):
        return self.wrapped[offset]

    def __len__(self):
        return len(self.wrapped)

    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])

    def __getattr__(self, name):
        return getattr(self.wrapped, name)

    def __repr__(self):
        return repr(self.wrapped)

    def __append__(self, other):
        return self.wrapped.append(other)

    def __contains__(self, element):
        if element in self.wrapped: return True
        else: return False

    def __reversed__(self):
        return reversed(self.wrapped)

    def __iter__(self):
        self.offset = 0
        return self

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item

if __name__ == '__main__':
    x = MyList('mielonka')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['jajka'])
    print(['szynka'] + x)
    print(x * 3)
    print(len(x))
    x.append('a')
    x.sort()
    print(''.join(c for c in x))
    print(list(reversed(x)))
