import sys
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def do(r, c):
    global cnt
    if g[r][c] == 1:
        g[r][c] = 0
        cnt += 1
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N and g[nr][nc] == 1:
                do(nr, nc)


N = int(input().strip())

count_list = []

g = [list(map(int, input().strip())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            cnt = 0
            do(i, j)
            count_list.append(cnt)
count_list.sort()
M = len(count_list)
print(M)
for k in range(M):
    print(count_list[k])

# BFS로 하면 조금 더 편할 것 같은데,
# 순환 자체는 어렵지 않았지만 숫자 처리를 어떻게 할 지 고민하느라 시간을 보냈다.
# DFS를 재귀로 쓰니, 숫자를 일일히 가져갈 수는 없는 노릇이고, 그냥 글로별 변수를 하나 선언해 주어서 사용했다.
