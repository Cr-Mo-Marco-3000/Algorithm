import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def do(r, c):
    Q = deque([(r, c)])
    visited[r][c] = 0
    while Q:
        r, c = Q.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if g[nr][nc] <= g[r][c]:
                    if visited[nr][nc] > visited[r][c] + 1:
                        visited[nr][nc] = visited[r][c] + 1
                        Q.append((nr, nc))
                elif g[nr][nc] > g[r][c]:
                    if visited[nr][nc] > (visited[r][c] + 1) + (g[nr][nc] - g[r][c]):
                        visited[nr][nc] = visited[r][c] + 1 + (g[nr][nc] - g[r][c])
                        Q.append((nr, nc))
    return visited[N-1][N-1]

for tc in range(1, T+1):
    N = int(input())
    g = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [[10000] * N for _ in range(N)]
    ans = do(0,0)
    print('#{} {}'.format(tc, ans))

