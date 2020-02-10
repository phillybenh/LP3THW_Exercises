#Alter Before or After
#using a built-in function called 'super', you can overide
#a parent function, but still call the parent version

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        #overides the Parent.altered
        print("CHILD, BEFORE PARENT altered()")
        #call super wiht arguments Child and self,
        # then call Parent.altered 
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()