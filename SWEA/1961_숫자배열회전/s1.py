import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    my_list = [list(map(int, input().split())) for _ in range(N)]

    i = 0
    # while문을 쓴다.
    print('#{}'.format(tc))
    while i < N:
        # i를 고정시킨 상태에서
        # 첫 번째 인덱스는 좌측 하단부터 위까지
        for j in range(N):
            print(my_list[N-1-j][i], end="")
        print(" ", end="")
        # 두 번째는 우측 하단부터 좌측 하단까지
        for k in range(N):
            print(my_list[N-1-i][N-1-k], end="")
        print(" ", end="")
        # 세 번째는 우측 상단부터 우측 하단까지
        for l in range(N):
            print(my_list[l][N-1-i], end="")
        print()
        i += 1




