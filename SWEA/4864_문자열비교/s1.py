import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    pattern = input()
    target = input()
    N = len(target)
    M = len(pattern)
    j = 0
    i = 0
    flag = 0
    cnt = 0
    while i < N - M + 1:
        cnt = 0
        j = 0
        while cnt < M:
            if target[i + j] == pattern[j]:
                j += 1
            if j == M:
                flag = 1
            cnt += 1
        i = i + 1

    print('#{} {}'.format(tc, flag))

