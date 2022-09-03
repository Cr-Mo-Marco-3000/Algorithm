import sys, collections

input = sys.stdin.readline
N, T = map(int, input().strip().split())

max_x = 0
max_y = 0
array = []

def do(r, c, cnt):
    global ans
    Q = collections.deque([(r, c, cnt)])
    while Q:
        r, c, w = Q.popleft()
        if r == T:
            g[r][c] = w
            ans = w
            return
        elif g[r][c] == -1:
            g[r][c] = w
            for i in range(r-2, r+3):
                for j in range(c-2, c+3):
                    if 0 <= i <= max_y and 0 <= j <= max_x:
                        if g[i][j] == -1:
                            Q.append((i, j, w + 1))


for _ in range(N):
    x, y = map(int, input().strip().split())
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    array.append((y, x))

g = [[0] * (max_x + 1) for _ in range(max_y + 1)]

while array:
    y, x = array.pop()
    g[y][x] = -1
g[0][0] = -1

ans = -1
do(0, 0, 0)

print(ans)

# 몬가 복잡한 문제 같지만 그냥 전형적인 bfs문제이다.
# 분류에 이진탐색이 있는 걸로 봐서는 이전 노드가 있는 부분을 탐색 범위에서 제외하는 등
# 방법이 있을 것 같다.