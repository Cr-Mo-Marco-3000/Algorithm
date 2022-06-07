# 트리 문제가 아니라 bfs 문제 같다.
# 1을 기준으로, 거리를 visited에 거리가 아니라, 부모를 기록한다.
from sys import stdin

def do(v):
    Q = [v]
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in g[v]:
            if not visited[w]:
                visited[w] = v
                Q.append(w)


N = int(stdin.readline().rstrip())

g = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, stdin.readline().rstrip().split())
    g[a].append(b)
    g[b].append(a)
visited = [0] * (N + 1)
do(1)

# visited에 부모를 기록하였으므로, 이를 출력한다.
for i in range(2, N+1):
    print(visited[i])
