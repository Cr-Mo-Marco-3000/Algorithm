import sys, collections
input = sys.stdin.readline

N, M = map(int, input().strip().split())

g = [tuple(map(str, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

delta_forward = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
delta_back = ((-1, 0, 'S'), (0, 1, 'W'), (1, 0, 'N'), (0, -1, 'E'))

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            # 역방향
            Q = collections.deque([(i, j)])
            while Q:
                r, c = Q.popleft()
                if not visited[r][c]:
                    visited[r][c] = 1
                    for w in range(4):
                        nr = r + delta_back[w][0]
                        nc = c + delta_back[w][1]
                        direction = delta_back[w][2]
                        if 0 <= nr < N and 0 <= nc < M and direction == g[nr][nc]:
                            Q.append((nr, nc))
            # 정방향
            nr, nc = i + delta_forward[g[i][j]][0], j + delta_forward[g[i][j]][1]
            while 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                nr, nc = nr + delta_forward[g[nr][nc]][0], nc + delta_forward[g[nr][nc]][1]

            cnt += 1
print(cnt)