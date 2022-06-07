import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    length = int(input())
    my_list = list(map(int, input().split()))
    # 선택정렬
    for i in range(len(my_list)-1):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

    print('#{} '.format(tc), end="")
    print(*my_list)

