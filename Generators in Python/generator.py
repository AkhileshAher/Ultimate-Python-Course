def my_generator():
    for i in range(50000):
        # Complex Computations
        yield i

gen = my_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


for j in gen:
    print(j)
