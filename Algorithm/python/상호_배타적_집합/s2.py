def make_set(x):
    p[x] = x

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[y] = x
    # p[find_set(y)] = find_set(x)

#1.
p = [0] * (6 + 1)
for i in range(len(p)):
    make_set(i)

print(p)
print('----------------------------------')

#2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

#3.
print(find_set(6))
print(find_set(3))
print(find_set(2))