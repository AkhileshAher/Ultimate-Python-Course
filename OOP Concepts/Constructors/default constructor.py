class Person:
    name="Tanuj"
    game="Chess"
    def __init__(self):
        print("Hey I am default constructor !!!")

    def func(self):
        print(f"Hello my name is {self.name} & I like to play{self.game}")

a=Person()
a.func()
