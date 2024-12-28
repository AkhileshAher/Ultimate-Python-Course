
try:
    a=int(input("Enter the number : "))
    print(a)


except ValueError:
    print("Number Entered is not an Intger")
except IndexError:
    print("Number entered is out of Index")


try:
    a=input("Enter the Number : ")
    b=[8,9,12,3]
    print(b[a])


except TypeError:
    print("List Indices Must be Integer or Slices not str")
