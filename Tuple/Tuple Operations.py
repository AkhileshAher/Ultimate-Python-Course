tuple1 = (0, 1, 2, 8, 2, 311, 1, 3, 2, 3)

res = tuple1.count(3)
print(res)

res = tuple1.index(3)
print(res)

res = tuple1.index(311)
print(res)

res = tuple1.index(3, 4, 8)
print(res)

res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
