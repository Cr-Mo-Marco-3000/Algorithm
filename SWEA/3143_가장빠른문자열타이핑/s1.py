import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 문자열, 패턴
    target, pattern = map(str, input().split())
    N = len(target) # 문자열 길이
    M = len(pattern) # 패턴 길이
    # x가 나오는 횟수라고 하자
    cnt = 0
    i = 0 # 문자열 인덱스
    while i < N - M + 1:
        for j in range(M):
            if target[i + j] != pattern[j]:
                break
        else:
            cnt += 1
            i += M - 1
        i += 1

    ans = N - (M * cnt) + cnt
    print('#{} {}'.format(tc, ans))

