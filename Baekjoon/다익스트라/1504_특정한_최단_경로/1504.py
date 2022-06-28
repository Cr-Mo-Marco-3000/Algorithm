import sys, heapq
input = sys.stdin.readline

def do(v):
    visited = [0] * (V+1)
    dist = [max_v] * (V+1)
    heap = [(0, v)]
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for nod, weight in g[v]:
                if not visited[nod] and dist[nod] > w + weight:
                    heapq.heappush(heap, (w + weight, nod))
    if visited[v1] and visited[v2] and visited[V]:
        return dist
    else:
        return False


max_v = sys.maxsize
V, E = map(int, input().strip().split())
g = [[] for _ in range (V+1)]

for _ in range(E):
    start, end, weight = map(int, input().strip().split())
    g[start].append((end, weight))
    g[end].append((start, weight))

v1, v2 = map(int, input().strip().split())

array1 = do(1)
if array1:
    array2 = do(v1)
    array3 = do(v2)
    print(min(array1[v1]+array2[v2]+array3[V], array1[v2]+array3[v1]+array2[V]))
else:
    print(-1)