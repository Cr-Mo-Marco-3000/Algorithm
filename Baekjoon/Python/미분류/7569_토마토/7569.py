import sys
from collections import deque

input = sys.stdin.readline

N, M, H = map(int, input().strip().split())

green_tomato = 0
Q = deque()
g = []
max_day = 0

for i in range(H):
    floor = []
    for j in range(M):
        temp = list(map(int, input().strip().split()))
        for k in range(N):
            if temp[k] == 0:
                green_tomato += 1
            elif temp[k] == 1:
                Q.append((i, j, k, 0))
        floor.append(temp)
    g.append(floor)

dh = (-1, 1, 0, 0, 0, 0)
dr = (0, 0, -1, 0, 1, 0)
dc = (0, 0, 0, 1, 0, -1)

while Q:
    h, r, c, d = Q.popleft()
    for w in range(6):
        nh = h + dh[w]
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nh < H and 0 <= nr < M and 0 <= nc < N:
            if g[nh][nr][nc] == 0:
                g[nh][nr][nc] = 1
                Q.append((nh, nr, nc, d + 1))
                green_tomato -= 1
                if max_day <= d + 1:
                    max_day = d + 1
if green_tomato:
    print(-1)
else:
    print(max_day)

# 2차원 배열에서 3차원으로 하나의 레이어만 올린 문제이다.
# 어려울 건 없다 차근차근히 진행하자
# 3차원도 마찬가지로, 0부터 아래, 혹은 위로 1층씩 쌓인다고 생각하면 편하다.