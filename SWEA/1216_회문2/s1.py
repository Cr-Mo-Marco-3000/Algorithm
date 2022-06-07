import sys

sys.stdin = open('input.txt')

T = 10

# 실패한 답안
for tc in range(1, T+1):
    tc = int(input())
    my_list = [list(map(str, input())) for _ in range(100)]
    max_length = 1
    i = 0
    for i in range(100):
        j = 0
        while j < 100:
            left = j
            right = j
            cnt = 1
            # my_list[i][left:right+1] == my_list[i][left:right+1][::-1]
            while left >= 0 and right <= 99 and my_list[i][left:right+1] == my_list[i][left:right+1][::-1]:
                # 왼쪽, 오른쪽에 -1, +1 해서는 짝수를 못 잡아낸다.
                if cnt % 2:
                    left -= 1
                    cnt += 1
                elif not cnt % 2:
                    right += 1
                    cnt += 1
            if len(my_list[i][left+1:right]) >= max_length:
                max_length = len(my_list[i][left+1:right])
            j += 1

    my_list = list(zip(*my_list))
    for i in range(100):
        j = 0
        while j < 100:
            left = j
            right = j

            # my_list[i][left:right+1] == my_list[i][left:right+1][::-1]
            while left >= 0 and right <= 99 and my_list[i][left:right+1] == my_list[i][left:right+1][::-1]:
                if cnt % 2:
                    left -= 1
                    cnt += 1
                elif not cnt % 2:
                    right += 1
                    cnt += 1
            if len(my_list[i][left+1:right]) >= max_length:
                max_length = len(my_list[i][left+1:right])
            j += 1

    print('#{} {}'.format(tc, max_length))

import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    
    print('#{} '.format(tc, ))

