'''First Program'''

def average(a=5,b=4):
    sum=a+b
    print((sum)/2)
        
average(6)

'''Second Program'''
def average(a, b, c=1):
  print("The average is ", (a + b + c) / 2)

average(4, 6)
average(a=5,b=9)
c = average(5, 6, 7)
print(c)


"""Third Program"""

def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  return 7
  return sum / len(numbers)


"""Fourth Program"""

def name(**name):
  # print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")
