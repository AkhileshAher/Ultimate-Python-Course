i=0
while i<7:
    print(i)
    i=i+1

    if i==4:
        break

else:
    print("Sorry no i")


for x in range(5):
    print("Iteration no {} in for loop".format(x+1))

else:
    print("Else Block in Loop")

print("Out of Loop")
