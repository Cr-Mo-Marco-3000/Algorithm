import sys

input = sys.stdin.readline

N = int(input().strip())

g = [[" "] * N for _ in range(N)]
cnt = 0

cr = 0
while cr < N:
    i = cr
    j = N-1
    while i < N:
        g[i][j] = chr(65 + (cnt % 26))
        i += 1
        j -= 1
        cnt += 1
    cr += 1

for k in range(N):
    print(*g[k])

# 인덱스 컨트롤 문제지만 while문을 두 개 써 주는 걸 생각해 내 주는 게 까다로웠다.
# 조건에 따라 끊임없이 돌아가는 반복문을 돌릴 때는 while문이 편리하다.