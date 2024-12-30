a="Hello"
b="Hello"

print(a==b)     # Refers to values
print(a is b)   # Refers to exact memory location

a=None
b=None
print(a==b)      # Refers to values
print(a is b)    # Refers to exact memory location
print(a is None)

a=13
b=13

print(a==b)     # Refers to values
print(a is b)   # Refers to exact memory location
print(a is 13)
print(a==13)

a=(1,6)
b=(1,6)
print(a==b)
print(a is b)  # True Because Tuple is Immutable

a={1,3,6}
b={1,3,6}
print(a==b)
print(a is b) # False Because list and dictionary are mutable
