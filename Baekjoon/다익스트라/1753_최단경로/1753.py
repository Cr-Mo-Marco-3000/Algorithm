import sys, heapq

input = sys.stdin.readline

def do():
    heap = [(0, s)]
    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = d
            for end, weight in g[v]:
                heapq.heappush(heap, (d + weight, end))


V, E = map(int, input().strip().split())
s = int(input().strip())

# 방문 표시
visited = [0] * (V + 1)

# 갱신용 거리 리스트
dist = [200000] * (V+1)

# 출발 좌표는 거리가 0이므로 표시
dist[s] = 0

# 연결 표시용 그래프
g = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, w = map(int, input().strip().split())
    g[start].append((end, w))

do()

for i in range(1, V+1):
    if dist[i] == 200000:
        print('INF')
    else:
        print(dist[i])

# 기본적인 다익스트라 문제이다.

