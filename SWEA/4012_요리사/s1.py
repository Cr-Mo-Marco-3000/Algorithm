import sys, itertools

sys.stdin = open('input.txt')





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    my_list = []
    for i in range(N):
        my_list.append(i)
    a = list(itertools.combinations(my_list, N//2))

    # print('#{} '.format(tc, ))

