# An example of a Class Definition with Inheritance

# Define the classes
class Bookcase(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self): #str is a special function. Gets called on any datatype when it should be printed. 
        return self.prettyprint() #they give back a string

    def prettyprint(self):
        return "A Generic Bookcase"

class Billy(Bookcase):
    def __init__(self, width, height):
        super(Billy, self).__init__(width, height)
        self.color = "red"

    # Overridden method
    def prettyprint(self):
        pretty = "A Billy Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

class Hemnes(Bookcase):
    def __init__(self, width, height):
        super(Hemnes, self).__init__(width, height)

    # Overridden method
    def prettyprint(self):
        pretty = "A Fancy Hemnes Bookcase with dimensions %d x %d cm"
        return pretty % (self.width, self.height)

# Make an instance of the classes
gen = Bookcase(50, 100)
bil = Billy(80, 120)
hem = Hemnes(200, 180)

# Call one of the functions (methods) inside the instance
print hem.prettyprint()

# Other useful things
print "Type:\n %r\n %r\n %r" % (type(gen), type(bil), type(hem))
print "Raw:\n %r\n %r\n %r" % (gen, bil, hem)
print "Pretty:\n %s\n %s\n %s" % (gen, bil, hem)
print "Is Instance of Billy?: ", isinstance(gen, Billy)
print "Is Instance of Billy?: ", isinstance(bil, Billy)
print "Is Instance of Billy?: ", isinstance(hem, Billy)
