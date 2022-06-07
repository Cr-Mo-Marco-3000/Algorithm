N = int(input())

g = [[""] * N for _ in range(N)]

cnt = 0

for j in range(N):
    for i in range(N):
        if not j % 2:
            g[i][j] = chr((cnt % 26) + 65)
            cnt += 1
        else:
            g[N-1-i][j] = chr((cnt % 26) + 65)
            cnt += 1

for k in range(N):
    print(*g[k])

