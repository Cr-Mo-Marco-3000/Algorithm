import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    cnt_1 = [0] * 10
    cnt_2 = [0] * 10
    ans = 0
    my_list = tuple(map(int, input().split()))
    for i in range(4):
        # 1 3 5
        if i % 2:
            cnt_2[my_list[i]] += 1
        # 0 2 4
        else:
            cnt_1[my_list[i]] += 1
    for j in range(4, 12):
        if j % 2:
            cnt_2[my_list[j]] += 1
            if cnt_2[my_list[j]] == 3:
                ans = 2
                break
            else:
                cnt = 0
                for i in range(my_list[j] - 2, my_list[j] + 3):
                    if cnt == 3:
                        ans = 2
                        break
                    if 0 <= i < 10 and cnt_2[i] >= 1:
                        cnt += 1
                    else:
                        cnt = 0
                if cnt == 3:
                    ans = 2
                    break
        else:
            cnt_1[my_list[j]] += 1
            if cnt_1[my_list[j]] == 3:
                ans = 1
                break
            else:
                cnt = 0
                for i in range(my_list[j] - 2, my_list[j] + 3):
                    if cnt == 3:
                        ans = 1
                        break
                    if 0 <= i < 10 and cnt_1[i] >= 1:
                        cnt += 1
                    else:
                        cnt = 0
                if cnt == 3:
                    ans = 1
                    break


    print('#{} {}'.format(tc, ans))

