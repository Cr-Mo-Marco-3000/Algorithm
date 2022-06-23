import sys
input = sys.stdin.readline

def do(r, c, n):
    global S
    global flag
    criterion = g[r][c]
    half = n // 2
    for i in range(r, r + n):
         for j in range(c, c + n):
            if g[i][j] != criterion:
                flag = True
                S += ['(']
                S += do(r, c, half)
                S += do(r, c + half, half)
                S += do(r + half, c, half)
                S += do(r + half, c + half, half)
                S += ')'
                return []
    else:
        return [str(criterion)]

N = int(input().strip())
g = [list(map(int, input().strip())) for _ in range(N)]
S = []
flag = False
do(0, 0, N)

if not flag:
    print(g[0][0])
else:
    for i in S:
        print(i, end='')
