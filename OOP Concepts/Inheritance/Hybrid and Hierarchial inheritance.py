# Example of Hybrid Inheritance

class Baseclass:
    pass

class Derived1(Baseclass):
    pass

class Derived2(Baseclass):
    pass

class Derived3(Derived1,Derived2):
    pass


# Example of Hierarchial inheritance

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass
