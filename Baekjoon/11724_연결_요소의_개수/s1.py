import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

g = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    g[a].append(b)
    g[b].append(a)
ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        ans += 1
    stack = [i]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in g[v]:
                if not visited[w]:
                    stack.append(w)

print(ans)