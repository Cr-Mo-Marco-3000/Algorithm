from sys import stdin
from collections import deque
N = int(stdin.readline().rstrip())

g = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

cnt = 0
num_list = []

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 처음에 i, j를 아래에서 받는 변수명과 같은 r, j로 했다가
# 어떤 행의 다음 열을 체크하지 않고 넘어가버리는 일을 만들었다
# 함수를 쓰는 게 아니라면, 이런 변수 체크에 주의해야 한다!
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            num = 0
            cnt += 1
            Q = deque([(i, j)])
            while Q:
                r, c = Q.popleft()
                if g[r][c] == 1:
                    g[r][c] = 0
                    num += 1
                for w in range(4):
                    nr = r + dr[w]
                    nc = c + dc[w]
                    if 0 <= nr < N and 0 <= nc < N:
                        if g[nr][nc] == 1:
                            num += 1
                            g[nr][nc] = 0
                            Q.append((nr, nc))
            num_list.append(num)
print(cnt)
num_list.sort()
for i in range(cnt):
    print(num_list[i])


