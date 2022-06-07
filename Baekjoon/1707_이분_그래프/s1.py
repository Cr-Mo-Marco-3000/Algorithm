from sys import stdin

K = int(input())

for _ in range(K):
    N, M = map(int, input().split())
    g = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, stdin.readline().rstrip().split())
        g[a][b] = 1
        g[b][a] = 1
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            stack = [i]
            while stack:
                v = stack.pop()
                for w in range(1, N+1):
                    if g[v][w] and not visited[w]:
                        visited[w] = 1
                        stack.append(w)
    if cnt == 2:
        print('YES')
    else:
        print('NO')

