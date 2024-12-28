a= int(input("Enter The value between 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("Value is Not between 5 and 9")
else:
    print("You Entered Right Value")
