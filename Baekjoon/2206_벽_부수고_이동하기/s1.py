from collections import deque

def do():
    Q = deque([[0, 0]])
    while Q:
        r, c = Q.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[r][c][0]: # 만약 아직 벽을 부수지 않았을 때,
                    if g[nr][nc]: # 만약 벽이라면
                        visited[nr][nc] = [0, visited[r][c][1] + 1]
                        Q.append([nr, nc])
                    if not g[nr][nc]
                        
s
                    Q.append([nr, nc])









N, M = map(int, input().split())
dr = (-1, 0, 1, 0)
dc = (0, 1, -1, 0)
g = [list(map(int, input())) for _ in range(N)]
visited = [[1, 0] * M for _ in range(N)]
start = (0, 0)
end = (N-1, M-1)
do()

