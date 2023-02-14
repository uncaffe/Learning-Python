"""
Plik z ćwiczeniami do książki pt. "Python- wprowadzenie"
"""

"""
1.
"""

# a)
S = 'mielonka'
for i in S: print(ord(i))

# b).1
print(sum(ord(i) for i in S))

# b).2
x = 0
for i in S:
    x += ord(i)
print(x)

# c).1
list1 = []
for i in S:
    list1.append(ord(i))
print(list1)

# c).2
list1 = []
print(list(map(ord, S)))

# c).3
print([ord(i) for i in S])

"""
3.
"""

# 3.1
dict1 = {4:'d', 3:'c', 5:'e', 1:'a', 2:'b'}
keys1 = list(dict1.keys())
keys1.sort()
for i in keys1:
    print(i, ':', dict1[i])

# 3.2
for i in sorted(dict1):
    print(i, ':', dict1[i])

"""
4.
"""

# a)
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0
while i < len(L):
    if (2 ** X) == L[i]:
        print((2 ** X), 'odnaleziono pod indeksem', i)
        break
    i = i+1
else:       
    print((2 ** X), 'nie odnaleziono')

# b)
for j in L:
    if (2 ** X) == j:
        print((2 ** X), 'odnaleziono pod indeksem', L.index(j))
        break
else:       
    print((2 ** X), 'nie odnaleziono')

# c)
Z = 2 ** X
if Z in L:
    print(Z, 'odnaleziono pod indeksem', L.index(Z))
else:       
    print((Z), 'nie odnaleziono')

# d).1
y = 0
for n in range(len(L)):
    L.append(2 ** y)
    L.pop(0)
    y += 1
print(L)

# d).2
L = []
for m in range(7): L.append(2 ** m)
print(L)

# f)
L = list(map(lambda x: 2 ** x, range(7)))
print(L)
