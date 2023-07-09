"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 25 """

''' 1. '''

def countlines(name):
    return len(open(name).readlines())

def forcountlines(name):
    x = 0
    for line in open(name):
        x += 1
    return x

def countchars(name):
    return len(open(name).read())

def forcountchars(name):
    x = 0
    for char in open(name).read():
        x += 1
    return x

def test(name):
    return countlines(name), countchars(name)
