import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 하나의 케이스마다, 리스트를 받는데, 항목들이 1로만 이루어진 리스트를 받는다.
    my_list = [[1] * i for i in range(1, N+1)]
    # 두 번째 줄까지는 항목들이 모두 1이니 상관 없고, 세 번째 줄부터, 인덱스 1 ~ i-1 까지는 이전 줄의 자신 + 자신-1 인덱스의 합
    for i in range(N):
        if i >= 2:
            for j in range(1, i):
                my_list[i][j] = my_list[i-1][j] + my_list[i-1][j-1]
    print(f'#{tc}')
    for k in range(N):
        for l in range(len(my_list[k])):
            print(my_list[k][l], end=' ')
        print()
        # print(*my_list[k])