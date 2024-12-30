numbers =[1,4,6,3,5]

# MAP FUNCTION
def cube(x):
    return x**3

data = list(map(cube,numbers))
print(data)


# We can also do this job using Lambda functions

data=list(map(lambda x : x*x*x , numbers))
print(data)
