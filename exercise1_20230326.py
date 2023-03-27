"""
Exercises for the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 15 """

''' 1. '''

S = 'spam'                      # a)
for i in S: print(ord(i))

print(sum(ord(i) for i in S))   # b).1

x = 0                           # b).2
for i in S:
    x += ord(i)
print(x)

list1 = []                      # c).1
for i in S:
    list1.append(ord(i))
print(list1)

list1 = []                      # c).2
print(list(map(ord, S)))

print([ord(i) for i in S])      # c).3

''' 3. '''

dict1 = {4:'d', 3:'c', 5:'e', 1:'a', 2:'b'} # 3.1
keys1 = list(dict1.keys())
keys1.sort()
for i in keys1:
    print(i, ':', dict1[i])

for i in sorted(dict1):                     # 3.2
    print(i, ':', dict1[i])

''' 4. '''

L = [1, 2, 4, 8, 16, 32, 64]                    # a)
X = 5

i = 0
while i < len(L):
    if (2 ** X) == L[i]:
        print((2 ** X), 'found at position', i)
        break
    i = i+1
else:       
    print((2 ** X), 'not found')

for j in L:                                     # b)
    if (2 ** X) == j:
        print((2 ** X), 'found at position', L.index(j))
        break
else:       
    print((2 ** X), 'not found')

Z = 2 ** X                                      # c)
if Z in L:
    print(Z, 'found at position', L.index(Z))
else:       
    print((Z), 'not found')

y = 0                                           # d).1
for n in range(len(L)):
    L.append(2 ** y)
    L.pop(0)
    y += 1
print(L)

L = []                                          # d).2
for m in range(7): L.append(2 ** m)
print(L)

L = list(map(lambda x: 2 ** x, range(7)))       # f)
print(L)

""" Chapter 18 """

''' 1. '''

def func(a, b=4, c=5): print(a, b, c)

func(1, 2)                              # result: 1 2 5

''' 2. '''

def func(a, b, c=5): print(a, b, c)

func(1, c=3, b=2)                       # result: 1 2 3

''' 3. '''

def func(a, *pargs): print(a, pargs)

func(1, 2, 3)                           # result: 1 (2, 3)

''' 4. '''

def func(a, **kargs): print(a, kargs)

func(a=1, c=3, b=2)                     # result: 1 {'c':3, 'b':2}

''' 5. '''

def func(a, b, c=3, d=4): print(a, b, c, d)

func(1, *(5, 6))                        # result: 1 5 6 4

''' 6. '''

def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
l=1; m=[1]; n={'a':0}
func(1, m, n)
print(l, m, n)                          # result: 1 ['x'] {'a': 'y'}'

print('\n')

def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        print(front, ';', items,';', tot)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

print(sumtree([1, [2, [3, 4], 5], 6]))
print('\n')
print(sumtree([[[[[1], 2], 3], 4], 5]))

print('-' * 50)

def knights():
    title = 'sir'
    action = (lambda x: title + ' ' + x)
    
    return action

act = knights()
msg = act('robin')
print(msg)
print(act)

""" Chapter 21 """

''' 2. '''

def adder(x, y): return x + y

print(adder('g', 'b'))
print(adder([3], ['s']))
print(adder(6.5, 9.5))

''' 3. '''

def adder(*x):
    res = x[0]
    for i in x[1:]:
        res += i
    return res

print(adder(6, 9, 69))
print(adder('g', 'b', 'gb'))
print(adder([3], ['s'], ['ome']))

''' 4. '''

def adder(**x):
    values = list(x.values())
    res = values[0]
    for i in values[1:]:
        res += i
    return res

D = dict(a=6, b=9, c=50)
print(adder(**D))

''' 5. '''

def copyDict(old):          # 5.1
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

D1 = dict(a=2, b=5)
print(copyDict(D1))

D2 = D1.copy()              # 5.2
print(D2)

def addDict(d1, d2):        # 6.1
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new

D3 = dict(c=9)
print(addDict(D1, D2))
print(addDict(D1, D3))

D1.update(D3)               # 6.2
print(D1)

''' 8. '''

def f1(y):                                      # 8.1
    if y <= 1:
        print(y, 'is not a prime number')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has a factor of', x)
                break
            x -= 1
        else:
            print(y, 'is aprime number')

def f2(y):                                      # 8.2 generator
    if y <= 1:
        return y, 'is not a prime number'
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                return y, 'has a factor of', x
                break
            x -= 1
        else:
            return y, 'is a prime number'

''' 9. '''

import math

L = [2, 4, 9, 16, 25]

S1 = []
for x in L: S1.append(math.sqrt(x))
print(S1)

S2 = list(map(lambda x: math.sqrt(x), L))
print(S2)

S2v2 = list(map(math.sqrt, L))
print(S2v2)

S3 = print([math.sqrt(x) for x in L])

S4 = list(math.sqrt(x) for x in L)
print(list(S4))

''' 10. '''

# timeseqs_all module result:

'''
3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
sqrt(x)
forLoop  : 1629428700.00000 => [0.0...99.99499987499375]
listComp : 1378884200.00000 => [0.0...99.99499987499375]
mapCall  : 1035847700.00000 => [0.0...99.99499987499375]
genExpr  : 1893910000.00000 => [0.0...99.99499987499375]
genFunc  : 1826098800.00000 => [0.0...99.99499987499375]
3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
x ** .5
forLoop  : 2131325000.00000 => [0.0...99.99499987499375]
listComp : 2039666200.00000 => [0.0...99.99499987499375]
mapCall  : 2507531400.00000 => [0.0...99.99499987499375] #lambda
genExpr  : 2356155600.00000 => [0.0...99.99499987499375]
genFunc  : 2430970600.00000 => [0.0...99.99499987499375]
3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]
pow(x, .5)
forLoop  : 2345216600.00000 => [0.0...99.99499987499375]
listComp : 2186066600.00000 => [0.0...99.99499987499375]
mapCall  : 2651988400.00000 => [0.0...99.99499987499375] #lambda
genExpr  : 2636976900.00000 => [0.0...99.99499987499375]
genFunc  : 1992182400.00000 => [0.0...99.99499987499375]
'''

''' 11. '''

def f1(x):                          # 11.1
    if x < 1:
        print('stop')
    else:
        print(x, end=' ')
        f1(x-1)

f1(5)                               # result: 5 4 3 2 1 stop

def f2(x):                          # 11.2
    if x < 1:
        yield 'stop'
    else:
        yield x
        for i in f2(x-1): yield i

list(f2(5))                         # result: [5 4 3 2 1 stop]

def f3(x):                          # 11.3 
    if x < 1:
        yield 'stop'
    else:
        yield from f(x-1)

list(f2(5))                         # result: 4 3 2 1 stop, TypeError: 'NoneType' object is not iterable

''' 12. '''

from math import factorial
from functools import reduce
from timeit import repeat

# all functions below work for positive integers only

def f1(x):
    if x < 1:
        return 1
    else:
        return x * f1(x-1)

def f2(x): return reduce(lambda n, m: n * m, list(range(1, x+1)))

def f3(x):
    lis = list(range(1, x+1))
    res = reduce((lambda n, m: n * m), lis)
    return res

def f4(x):
    y = x
    while x > 1:
        y = y * (x-1)
        x -= 1
    return y

def f5(x):
    res = 1
    for i in range(1, x+1): res *= i
    return res

def f6(x):
    return factorial(x)

n = 6
print(f1(n), f2(n), f3(n), f4(n), f5(n), f6(n))

for test in (f1, f2, f3, f4, f5, f6):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=100, repeat=3)))
