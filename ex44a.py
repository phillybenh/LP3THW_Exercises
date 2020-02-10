#ex44a.py
#showing IMPLICIT INHERITANCE
#implicit actions happen when a function is defined in the parent,
#but not in the child

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()