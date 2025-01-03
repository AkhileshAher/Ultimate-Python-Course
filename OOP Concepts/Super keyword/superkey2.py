class Parent:
    def parentmethod(self):
        print("I am Parent method 1 ")

class Child(Parent):
    def childmethod(self):
        print("I am Child class method 2 ")
        super().parentmethod()

parent = Parent()
child = Child()

child.parentmethod()
child.childmethod()
