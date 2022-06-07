import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 저글링의 수
zerg = 0

# 최대값
max_v = 3

def do(r, c):
    global max_v
    global zerg
    Q = deque([[r, c, 3]])
    visited[r][c] = 3
    while Q:
        r, c, v = Q.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and g[nr][nc]:
                    zerg -= 1
                    visited[nr][nc] = v + 1
                    Q.append([nr, nc, v + 1])
                    if max_v < v + 1:
                        max_v = v + 1


g = []

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

for i in range(M):
    temp = tuple(map(int, input().rstrip()))
    for j in range(N):
        if temp[j] == 1:
            zerg += 1
    g.append(temp)

visited = [[0] * N for _ in range(M)]
sc, sr = map(int, input().strip().split())

do(sr-1, sc-1)
print(max_v)
print(zerg-1)

# 사소한 값인 시작값과 최대값 설정을 서투루 했다가 값에 오류가 났다.
# 시작값은 주어진 시작지점의 좌표가 1부터 시작한다는 점을 체크하지 않아 미스가 났고
# 최대값은 처음 저글링만 감염될 때를 고려하지 않아 3으로 설정하지 않았다.
# 문제에서 주어진 대로! 설정하자!