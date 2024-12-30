numbers=[1,5,7,9,3,4]
# FILTER FUNCTION

def filter_function(a):
    return a>4

datafiltered = list(filter(filter_function,numbers))
print(datafiltered)

# This can be done using lambda functions

datafiltered = list(filter(lambda x : x>4,numbers))
print(datafiltered)
