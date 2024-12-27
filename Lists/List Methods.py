l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(7)
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)
print(l.index(1))
print(l.count(1))


m = l.copy()
m[0] = 0

l.insert(1, 899)
print(l)

m = [900, 1000, 1100]
k = l + m
print(k)

l.extend(m)
print(l)
