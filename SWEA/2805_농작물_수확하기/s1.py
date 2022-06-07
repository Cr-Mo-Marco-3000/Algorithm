import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    my_list = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range((N // 2)):
        for j in range((N // 2)-i, (N // 2) + i + 1):
            total += my_list[i][j]
            total += my_list[N-1-i][j]
    total += sum(my_list[(N // 2)])

    print('#{} {}'.format(tc, total))

