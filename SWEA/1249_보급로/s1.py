import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def do(r, c, value):
    Q = deque([(r, c, value)])
    while Q:
        r, c, value = Q.popleft()
        if visited[r][c] > value:
            visited[r][c] = value
            for w in range(4):
                nr = r + dr[w]
                nc = c + dc[w]
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] > visited[r][c] + g[nr][nc]:
                        Q.append((nr, nc, visited[r][c] + g[nr][nc]))
    return visited[N-1][N-1]



for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input())) for _ in range(N)]
    visited = [[100000] * N for _ in range(N)]
    ans = do(0, 0, 0)
    print('#{} {}'.format(tc, ans))

