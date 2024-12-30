class Person:   # CLASS
    name="Akhilesh"
    age=19
    designation="Software Developer"

    def Student(self):
        print(f"{self.name} is working as {self.designation} and just {self.age} years old")

a=Person()      # OBJECT CREATED
b=Person()      # OBJECT CREATED

print(a.name)
a.Student()

a.name="Yuvraj"
a.age=22
a.designation="HR"
a.Student()

b.name="Mayuresh"
b.age=18
b.designation="Core Java Developer"
b.Student()
