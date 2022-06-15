# V, E = map(int, input().split())

# p = [i for i in range(V+1)]

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


# def kruskal():
#     global ans
#     edge_cnt = idx = 0


p = [i for i in range(11)]

union(1, 2)
union(2, 3)
union(3, 4)
union(2, 5)
union(2, 6)
print(find_set(4))
