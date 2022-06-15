import sys

input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    ans = edge_cnt = idx = 0
    while edge_cnt < V-1:
        x = edges[idx][0]
        y = edges[idx][1]
        if find_set(x) != find_set(y):
            edge_cnt += 1
            ans += edges[idx][2]
            union_set(x, y)
        idx += 1
    return ans

V, E = map(int, input().strip().split())

edges = [list(map(int, input().strip().split())) for _ in range(E)]

# 람다식은 매개변수 x를 받고, x[2]를 return하는 식이다
# key로는 다음과 같이 쓸 수 있다.

p = [i for i in range(V+1)]

edges.sort(key=lambda x: x[2])

print(kruskal())