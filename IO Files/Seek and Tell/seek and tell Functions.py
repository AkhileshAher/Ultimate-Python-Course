
with open('text1.txt','w') as f:
    f.write("Hello World2!!")

with open('text1.txt','r') as file:
    print(type(file))

    file.seek(10) # Move Pointer to 10 byte in file
    print(file.tell()) # Gives Current Position of Pointer
    print(file.read())
