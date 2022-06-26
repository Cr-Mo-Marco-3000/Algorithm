import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().strip().split())
g = [[] for _ in range(V+1)]


for i in range(E):
    start, end, weight = map(int, input().strip().split())
    g[start].append((end, weight))
    g[end].append((start, weight))

u, v = map(int, input().strip().split())

def do(start):
    visited = [0] * (V+1)
    dist = [sys.maxsize] * (V+1)
    heap = [(0, start)]
    while heap:
        w, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = w
            for i in g[node]:
                if not visited[i][0] and dist[i][0] > w + g[node][i][1]:
                    heapq.heappush(heap, (w + g[node][i], i))


    return visited

S = do(1)
U = do(u)
V = do(v)

# 경우의 수 2가지
# 더 적게 드는 것 구하자
# 1 => u => v => N
# 1 => v => u => N
