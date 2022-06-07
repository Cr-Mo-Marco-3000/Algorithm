import sys

sys.stdin = open('input.txt')

T = int(input())
# N: 총 배열의 좌우 길이
# M: 파리채 좌우 길이

for tc in range(1, T+1):
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]
    # 파리채 index의 범위
    # i <= N - M
    max_num = 0
    total = 0
    for i in range(N-M+1): # 배열 인덱스
        for j in range(N-M+1): # 배열 인덱스 순환
            for k in range(M): # 파리채 블로킹 순환
                for l in range(M): # 파리채 인덱스 순환
                    total += space[i+k][j+l]
            if total > max_num: # 다 더해준 후, 기존 최대값보다 크다면
                max_num = total # 갱신
            total = 0

    print('#{} {}'.format(tc, max_num))
