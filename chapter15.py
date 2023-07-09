"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
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
