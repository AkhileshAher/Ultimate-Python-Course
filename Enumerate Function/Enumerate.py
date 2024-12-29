marks=[12,56,98,32,65,74,56]
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Awesome , Akhilesh")


# If we want to change index
print("New Program")
marks=[12,56,98,32,65,74,56]
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("Awesome , Akhilesh")


# To Print Index and Elements

fruits=["Mango","Apple","Banana","Guava","Grapes"]
for index,juices in enumerate(fruits):
    print(f"The index of {juices} is {index}")
