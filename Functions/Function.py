def calculateGmean(a,b):
    Gmean=(a*b)/(a+b)
    print(Gmean)

def isGreater(a,b):
    if(a<b):
        print("B is Greater")
    else:
        print("A is Greater")

a=10
b=12
calculateGmean(a,b)
isGreater(a,b)

c=6
d=5
calculateGmean(c,d)
isGreater(c,d)
