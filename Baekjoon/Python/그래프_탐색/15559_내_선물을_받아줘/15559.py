import sys, collections

input = sys.stdin.readline

N, M = map(int, input().strip().split())

g = [tuple(map(str, input().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
delta_forward = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
delta_back = ((-1, 0, 'S'), (0, 1, 'W'), (1, 0, 'N'), (0, -1, 'E'))

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            Q = collections.deque([(i, j)])
            while Q:
                r, c = Q.popleft()
                if not visited[r][c]:
                    visited[r][c] = 1
                    direction_f = g[r][c]
                    for w in range(4):
                        nr = r + delta_back[w][0]
                        nc = c + delta_back[w][1]
                        direction_b = delta_back[w][2]
                        if 0 <= nr < N and 0 <= nc < M and direction_b == g[nr][nc]:
                            Q.append((nr, nc))
                        elif delta[w] == delta_forward[direction_f]:
                            Q.append((r + delta[w][0], c + delta[w][1]))
            cnt += 1

print(cnt)