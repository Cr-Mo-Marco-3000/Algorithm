N = int(input())

g = [[""] * N for _ in range(N)]

cnt = 0

for j in range(N):
    for i in range(N):
        g[N-1-i][N-1-j] = chr((cnt % 26) + 65)
        cnt += 1
for k in range(N):
    print(*g[k])

