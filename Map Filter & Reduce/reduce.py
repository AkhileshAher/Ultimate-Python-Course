numbers=[1,5,6,7,3,2]
# REDUCE FUNCTION
from functools import reduce
def sumlist(x,y):
    return x+y

datareduced = reduce(sumlist,numbers)
print(datareduced)

# This can be done using lambda function

datareduced = reduce(lambda x,y : x+y,numbers)
print(datareduced)
