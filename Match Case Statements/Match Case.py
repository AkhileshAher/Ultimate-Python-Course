x=int(input("Enter the Value of x : "))

match x:
    case 0:
        print(x,"is 0")
    case 4:
        print(x,"is 4")
    case _ if(x!=80):
        print(x,"is not 80")
    case _ if(x!=90):
        print(x,"is not 90")
    case _ :
        print("This is Default Case")
