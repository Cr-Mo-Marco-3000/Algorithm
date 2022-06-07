import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(s):
    global cnt
    if s != 0:
        do(g[s][0])
        g[s][1] = cnt
        cnt += 1
        do(g[s][2])


for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    g = [[0, 0, 0] for _ in range(N + 1)]
    for i in range(1, N+1):
        if g[i//2][0] == 0:
            g[i//2][0] = i
        else:
            g[i//2][2] = i

    do(1)
    print('#{} {} {}'.format(tc, g[1][1], g[N//2][1]))
