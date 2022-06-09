N = int(input())

g = [[0] * N for _ in range(N)]

cnt = 1
r = 0
c = N // 2
g[r][c] = cnt
while cnt < N * N:
    # 숫자가 N의 배수
    if not cnt % N:
        r += 1
        cnt += 1
        g[r][c] = cnt
    else:
        r -= 1
        c -= 1
        if r == -1:
            r = N-1
        if c == -1:
            c = N-1
        cnt += 1
        g[r][c] = cnt

for i in range(N):
    print(*g[i])