import sys

sys.stdin = open('sample_input.txt')


def do(r, c, cnt):
    global ans
    if g[r][c] == 3 and cnt - 1 > ans:
        ans = cnt - 1
        return
    elif ans and cnt - 1 > ans:
        return
    elif g[r][c] == 0:
        g[r][c] = 1
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N:
            if not g[nr][nc]:
                do(nr, nc, cnt + 1)
                g[nr][nc] = 0
            elif g[nr][nc] == 3:
                do(nr, nc, cnt + 1)

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    g = []
    ans = 0
    for i in range(N):
        temp = list(map(int, input()))
        for j in range(N):
            if temp[j] == 3:
                target = [i, j]
            elif temp[j] == 2:
                start = [i, j]
        g.append(temp)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    do(start[0], start[1], 0)

    print('#{} {}'.format(tc, ans))

