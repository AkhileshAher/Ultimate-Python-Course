# USING SIMPLE OPERATORS
foods = list()
while True:
    food= input("What food do you like : ")
    if(food=="quit"):
        break
    foods.append(food)



# Using Walrus Operator
foods = list()
while (food:=input("What food do you like : "))!="quit":
    foods.append(food)
