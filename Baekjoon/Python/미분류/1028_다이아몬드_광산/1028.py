import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

g = [list(map(int, input().strip().split())) for _ in range(N)]
# M 3 => 최대 5, 4일때 7

dr = (1, 1, -1, -1)
dc = (-1, -1, 1, 1)

def do(r, c, crit):
    crit -= 1
    nr, nc = -1, -1
    while nr != r or nc != c:
        nr, nc = r + dr[]
    else:
        return
ans = 0

crit = round(N // 2)

for i in range(N):
    for j in range(M):
        if g[i][j]:
            do(i, j, crit)
