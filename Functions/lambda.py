# def double(x):
#     return x*2

def appl(fx, value):
  return 6 + fx(value)
print(appl(lambda x: x * x , 2))

# lambda arguments : expression

double = lambda x : x*2
square = lambda x : x*x
cube = lambda x : x**3

print(double(8))
print(square(5))
print(cube(3))
