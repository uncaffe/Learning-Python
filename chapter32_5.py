"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 5. '''

from setwrapper import Set

#a)
s1 = Set([8, 9, 10, 11, 12])
s2 = Set([10, 11, 12, 13, 14])

s1 & s2
s1 | s2

#b)
s3 = Set('Monty Python')
s3[0]
s3[-3]

#c)
for i in s3: print(i, end=' ')

#d)
s3 & 'ham'
s3 | 'ham'

class MySet(Set):
    def intersect(self, *others):   #or def intersect(*others)
        res = []
        for x in self:              #or for x in others[0]
            for other in others:    #or for other in others[1:]
                if x not in other: break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for seq in args:
            for x in seq:
                if not x in res:
                    res.append(x)
        return Set(res)
