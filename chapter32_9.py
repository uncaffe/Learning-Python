"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """

''' 9. '''

class Actor:
    def line(self):
        print(self.name + ':', repr(self.says()))   # v2 print(self.__class__.__name__ + ':', repr(self.says()))        

class Customer(Actor):
    name = 'customer'                               # v2 to be deleted
    def says(self):
        return 'Un espresso per favore.'
    
class Clerk(Actor):
    name = 'clerk'                                  # v2 to be deleted
    def says(self):
        return '100$, bitch.'
    
class Parrot(Actor):
    name = 'parrot'                                 # v2 to be deleted
    def says(self):
        return 'Bitch, bitch, bitch...'

class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()
        
if __name__ == '__main__':
    Scene().action()
