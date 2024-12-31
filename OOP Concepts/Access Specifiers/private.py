class Student:
    def __init__(self,age,name):
        self.__age=age     # An indication of private variable
        
        def __funcName(self):   # An indication pf private Function
            self.y=34
            print(self.y)


class Subject(Student):
    pass


obj=Student(21,"Harry")
obj1=Subject

# Calling by object of Class Student
print(obj.__age)
print(obj.__funcName())

# Calling by object of class Subject
print(obj1.__age)
print(obj1.__funcName())




#OUTPUT
# Throws Errors as : 
'''
AttributeError: 'student' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
AttributeError: 'subject' object has no attribute '__age'
AttributeError: 'student' object has no method '__funName()'
'''


# The Program can be executed by using name mangling concept as
print(obj._Student__age)  # NAME MANGLING CONCEPT
