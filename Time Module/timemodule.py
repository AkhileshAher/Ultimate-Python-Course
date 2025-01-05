import time

def usingWhile():
    i=0
    while i < 5000:
        i=i+1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()

usingWhile()
print(time.time() - init)
print(t1)
