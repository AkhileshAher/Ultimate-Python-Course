from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")


print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")
print(fx(61))
print("Done for 61")
