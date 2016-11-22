class Parent(object):

    def override(self):
        print "PARENT override()" #defines what the override function of class Parent does

    def implicit(self):
        print "PARENT implicit()" #defines what the implicit function of class Parent does

    def altered(self):
        print "PARENT altered()" # defines what the altered function of class Paerent does

class Child(Parent):

    def override(self):
        print "CHILD override()" # overrides the override function form the parent class and makes it to the Child override function

    def altered(self): # overrides the altered function of the parent class
        print "CHILD, BEFORE PARENT altered()" # with this
        super (Child, self).altered() # then takes the altered function of the parent class and prints out
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
