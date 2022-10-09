# 아오 귀찮아
from sys import stdin
from collections import deque

def do(my_list):
    global max_v
    Q = deque(my_list)
    while Q:
        v = Q.popleft()
        r = v[0]
        c = v[1]
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if g[nr][nc] == 0:
                    g[nr][nc] = g[r][c] + 1
                    Q.append([nr, nc])
                    if g[nr][nc] > max_v:
                        max_v = g[nr][nc]



M, N = map(int, stdin.readline().rstrip().split())
zero_list = []
my_list = []
g = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
max_v = 0

for i in range(N):
    temp = list(map(int, stdin.readline().rstrip().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            my_list.append([i, j])
        elif temp[j] == 0:
            zero_list.append([i, j])
    g.append(temp)

do(my_list)

if not zero_list:
    print(0)
else:
    for x in range(N):
        for y in range(M):
            if g[x][y] == 0:
                print(-1)
                break
        if g[x][y] == 0:
            break
    else:
        print(max_v-1)

