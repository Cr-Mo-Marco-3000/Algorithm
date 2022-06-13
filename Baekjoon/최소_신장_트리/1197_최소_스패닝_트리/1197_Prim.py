import sys, heapq

input = sys.stdin.readline

def do():
    ans = 0
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            ans += w
            for way, weight in g[v]:
                if not visited[way]:
                    heapq.heappush(heap, (weight, way))
    return ans

V, E = map(int, input().strip().split())

g = [[] for _ in range(V + 1)]

visited = [0] * (V + 1)

for i in range(E):
    start, end, weight = map(int, input().strip().split())
    g[start].append((end, weight))
    g[end].append((start, weight))

print(do())

# 최소 신장 트리의 전형 같은 문제이다.
# SWEA에서 돌렸던 것과 비슷하기 때문에 복습하는 느낌으로 해 보았다.