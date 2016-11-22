# An example of a Class Definition with Inheritance

# Define the classes
class Bookcase(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self): #str is a special function. Gets called on any datatype when it should be printed. See line 45!
        return self.prettyprint() #they give back a string

    def prettyprint(self):
        return "A Generic Bookcase"

class Billy(Bookcase): #definition of the class: Name (which class does it extend/from which class is it the child class?)
    def __init__(self, width, height):
        super(Billy, self).__init__(width, height) #super overrides the method - calls the initializing init method
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
print "Type:\n %r\n %r\n %r" % (type(gen), type(bil), type(hem)) #type gives the type of data
print "Raw:\n %r\n %r\n %r" % (gen, bil, hem) #prints out just the object itself, getting the raw display of it: Type, name, location in memory
print "Pretty:\n %s\n %s\n %s" % (gen, bil, hem) # gives out the result of the prettyprint function - but actually of the str function! str is sth python looks for if it should give out sth pretty
print "Is Instance of Billy?: ", isinstance(gen, Billy)
print "Is Instance of Billy?: ", isinstance(bil, Billy)
print "Is Instance of Billy?: ", isinstance(hem, Billy)
