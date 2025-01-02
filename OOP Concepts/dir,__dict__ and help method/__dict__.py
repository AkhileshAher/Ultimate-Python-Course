class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person("John Snow",30)
print(person.__dict__)

'''The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection'''
