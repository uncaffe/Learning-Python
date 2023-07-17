"""
Exercises from the book "Learning Python, 5th Edition" by Mark Lutz.
"""

""" Chapter 32 """
'''  6. '''

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via 
    inheritance of __str__ coded here;  displays instance attrs only;  self is
    instance of lowest class; __X names avoid clashing with client's attrs
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           self.__supers(),                 # The extension
                           id(self),                        # My address
                           self.__attrnames())              # name=value list
    def __supers(self):                                     # The extension
        names = []
        for super in self.__class__.__bases__:
            names.append(super.__name__)
        return ', '.join(names)

if __name__ == '__main__': 
    import testmixin
    testmixin.tester(ListInstance)
