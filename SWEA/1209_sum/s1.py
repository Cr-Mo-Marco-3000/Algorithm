import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    a = int(input())
    my_list = [list(map(int, input().split())) for _ in range(100)]
    max_value = sum(my_list[0]) # 음수 있을까봐 초기값을 잡아줬다.
    total = 0
    for i in range(100): # 행 총합들 비교
        for j in range(100):
            total += my_list[i][j]
        if total > max_value:
            max_value = total
        total = 0

    for i in range(100): # 열 총합들 비교
        for j in range(100):
            total += my_list[j][i]
        if total > max_value:
            max_value = total
        total = 0

    for i in range(100): # 대각선 비교
        total += my_list[i][i]
    if total > max_value:
        max_value = total
    total = 0

    for i in range(100): # 역대각선 비교
        total += my_list[i][99 - i] #0, len(my_list) - 1 => 1, len(my_list - 2
    if total > max_value:
        max_value = total

    print('#{} {}'.format(tc, max_value))

