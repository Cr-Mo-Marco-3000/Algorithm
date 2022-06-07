import sys

sys.stdin = open('input.txt')

T = int(input())

# 가로, 세로 인덱스의 범위
# 가로, 0 ~ N-M => range(N-M+1)로 지정
# 세로, 0 ~ N-M => range(N-M+1)로 지정

for tc in range(1, T+1):
    N, M = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += g[i+k][j+l]
            if total > max_v:
                max_v = total
    print(f'#{tc} {max_v}')
