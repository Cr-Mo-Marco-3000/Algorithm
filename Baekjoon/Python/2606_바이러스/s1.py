from sys import stdin
from collections import deque

V = int(stdin.readline().rstrip())
E = int(stdin.readline().rstrip())
g= [[] for _ in range(V+1)]

for i in range(E):
    start, end = map(int, stdin.readline().rstrip().split())
    g[start].append(end)
    g[end].append(start)

Q = deque([1])
visited = [0] * (V+1)
cnt = 0
while Q:
    v = Q.popleft()
    for w in g[v]:
        if not visited[w]:
            visited[w] = 1
            cnt += 1
            Q.append(w)
print(cnt-1)