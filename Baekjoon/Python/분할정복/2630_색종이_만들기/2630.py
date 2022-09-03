import sys

input = sys.stdin.readline

def do(r, c, N):
    criterion = g[r][c]
    half = N // 2
    for i in range(r, r + N):
        for j in range(c, c + N):
            if g[i][j] != criterion:
                do(r, c, half)                  # 2사분면
                do(r + half, c, half)           # 3사분면
                do(r, c + half, half)           # 1사분면
                do(r + half, c + half, half)    # 4사분면
                return
    else:
        color[criterion] += 1
        return

N = int(input().strip())

g = [tuple(map(int, input().strip().split())) for _ in range(N)]

# 1: blue, 0: white
color = {1: 0, 0: 0}

# left, right, up, down
do(0, 0, N)

print(color[0])
print(color[1])
