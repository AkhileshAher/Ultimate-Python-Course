class Employee:                 # PARENT CLASS EMPLOYEE
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print(f"The Employee id {self.id} is of {self.name}")

class Programmer(Employee):   # CHILD CLASS PROGRAMMER
    def language(self):
        print("The Default language is Python ")

e1 = Employee("Akhilesh Aher",101)     # INSTANCE OF PARENT CLASS
e1.show_details()

e2 = Programmer("Bhairav",560)          # INSTANCE OF CHILD CLASS
e2.language()
