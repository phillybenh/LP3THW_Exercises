#Overriding Explicitly
#explicitly defining a function in a child can be used to 
#effectively replace the functionality of a parent

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
