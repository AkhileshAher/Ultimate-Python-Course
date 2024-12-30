with open('text1.txt','w') as f:
    f.write("Hello World2!!")
    f.truncate(3)

with open('text1.txt','r') as f:
    print(f.read())
