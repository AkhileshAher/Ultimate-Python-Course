class Employee:
    
    def __init__(self,ename,job):
        self.ename=ename
        self.job=job
        print(f"Hello Myself {self.ename} my job {self.job}")
        print("Hello !! I am Parameterized Constructor")

    def func(self):
        print(f"Hello my name is {self.ename} & I like to play {self.job}")

b=Employee("Akhil","Cloud Engineer")
b.func()
b.ename="Rupesh"
b.job="SDE Intern"
b.func()
