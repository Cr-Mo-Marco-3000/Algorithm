import sys

sys.stdin = open('input.txt')


def do(sr, sc):
    global max_length
    global min_nod
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    stack = [[sr, sc]]
    while stack:
        v = stack.pop()
        r, c = v[0], v[1]
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N and g[nr][nc] == g[r][c] + 1:
                visited[nr][nc] = visited[r][c] + 1
                stack.append([nr, nc])

    if visited[r][c] > max_length:
        max_length = visited[r][c]
        min_nod = g[sr][sc]
    elif visited[r][c] == max_length:
        if g[sr][sc] < min_nod:
            min_nod = g[sr][sc]

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    max_length = 0
    min_nod = N*N

    for i in range(N):
        for j in range(N):
            do(i, j)

    print('#{} {} {}'.format(tc, min_nod, max_length))