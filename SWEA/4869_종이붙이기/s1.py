import sys

sys.stdin = open('input.txt')

T = int(input())

# 규칙이 왜 이렇게 나오는지는 모르겠다...
def square(N):
    if N == 1:
        return N
    if N == 2:
        return N + 1
    elif N > 2:
        return square(N-1) + square(N-2) * 2


for tc in range(1, T+1):
    a = int(input())
    N = a//10
    b = square(N)
    print('#{} {}'.format(tc, b))

