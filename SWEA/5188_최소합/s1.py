import sys

sys.stdin = open('sample_input.txt')

T = int(input())
dr = (-1, 0, 1, 0)
dc = (0, 1, -1, 0)
# 기본, 재귀로 풀어보기


def do(r, c, number):
    global ans
    number += g[r][c]
    if r == N-1 and c == N-1:
        if number < ans:
            ans = number
    elif number > ans:
        return
    else:
        if r < N-1:
            do(r+1, c, number)
        if c < N-1:
            do(r, c+1, number)


for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000000
    do(0, 0, 0)
    print(f'#{tc} {ans}')
