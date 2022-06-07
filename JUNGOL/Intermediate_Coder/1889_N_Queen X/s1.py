import sys
input = sys.stdin.readline


def do(t):
    global cnt
    if t == N:
        cnt += 1
        return
    else:
        for j in range(N):
            if g[t][j] == 0:
                my_stack = []
                r = t
                while r < N:

                    g[r][j] = 1
                do(t+1)


cnt = 0
N = int(input())
g = [[0] * N for _ in range(N)]
do(0)
