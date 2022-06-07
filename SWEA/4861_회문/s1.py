import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # N행 N열, M개의 글자
    N, M = map(int, input().split())
    my_list = [list(map(str, input())) for _ in range(N)]
    # 탐색 인덱스 k
    k = 0
    # 회문판별용 패턴 pattern
    palindrome = ''

    for i in range(N):
        k = 0
        for j in range(N - M + 1):
            pattern = my_list[i][j:j + M]
            while k < M // 2:
                if pattern[k] != pattern[M - 1 - k]:
                    break
                k += 1
                if k >= M // 2:
                    palindrome = pattern
            if palindrome == pattern:
                break
        if palindrome == pattern:
            break

    my_list = list(zip(*my_list))
    for i in range(N):
        k = 0 # 이 k 값을 안 줘서 오류가 났다. while을 쓸 때는 항상 초기화와 카운팅을 생각하자
        for j in range(N - M + 1):
            pattern = my_list[i][j:j + M]
            while k < M // 2:
                if pattern[k] != pattern[M - 1 - k]:
                    break
                k += 1
                if k >= M // 2:
                    palindrome = pattern
            if palindrome == pattern:
                break
        if palindrome == pattern:
            break
    palindrome = "".join(palindrome)
    print('#{} {}'.format(tc, palindrome))


