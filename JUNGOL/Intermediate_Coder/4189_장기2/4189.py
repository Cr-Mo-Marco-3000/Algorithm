import sys
from collections import deque
input = sys.stdin.readline

def do(r, c):
    Q = deque([(r, c, 0)])
    g[r][c] = -1
    while Q:
        r, c, v = Q.popleft()
        if r == S-1 and c == K-1:
            return v
        for w in range(8):
            nr, nc = r + delta[w][0], c + delta[w][1]
            if 0 <= nr < M and 0 <= nc < N:
                if not g[nr][nc]:
                    g[nr][nc] = v + 1
                    Q.append((nr, nc, v + 1))


delta = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

M, N = map(int, input().strip().split())

g = [[0] * (N) for _ in range(M)]

R, C, S, K = map(int, input().strip().split())

print(do(R-1, C-1))

# 문제 조건에, 장기판의 제일 왼쪽 위의 위치가 1,1이라고 했기 때문에,
# 받아주는 숫자들을 -1 한 상태로 계산해 주어야 오류가 나지 않는다.