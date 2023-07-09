"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

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
