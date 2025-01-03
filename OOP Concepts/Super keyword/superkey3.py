class Parent1:
    def parentmethod(self):
        print(" I am parent method 1 of Parent 1 class")

class Parent2:
    def parentmethod(self):
        print(" I am Parent method 2 of Parent 2 class")

class Child(Parent1,Parent2):
    def childmethod(self):
        print(" I am Child method of Child Class")
        super().parentmethod()
        

child = Child()
child.childmethod()
