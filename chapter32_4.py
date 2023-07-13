"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 4. '''

class Attrs:
    def __getattr__(self, name):
        print('get %s' % name)
    def __setattr__(self, name, value):
        print('set {0} = {1}'.format(name, value))

