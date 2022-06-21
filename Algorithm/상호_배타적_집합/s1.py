def make_set(x):
    p[x] = x

def find_set(x):
    # 반복
    # while x != p[x]:
    #     x = p[x]
    # return x

    # 재귀
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    # x, y = find_set(x), find_set(y)
    p[find_set(y)] = find_set(x)

# 1.
# p = [0] * (6 + 1)
# for i in range(7):
#     make_set(i)

p = list(range(7))
print(p)
print('----------------------------------')

# 2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

# 3.
print(find_set(6))
print(find_set(3))
print(find_set(2))