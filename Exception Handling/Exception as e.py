a=input("Enter the Number : ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e:
    print(e)
    print("Invalid Input")

print("Some imp Lines of Code")
print("End of the Program")
