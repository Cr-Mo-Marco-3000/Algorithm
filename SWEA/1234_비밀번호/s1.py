import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, my_list = map(str, input().split())
    N = int(N)
    my_list = list(map(int, my_list))
    i = 0
    flag = True
    while flag == True:
        flag = False
        while i < len(my_list)-1:
            if my_list[i] == my_list[i+1]:
                my_list.pop(i)
                my_list.pop(i)
                i = i - 1
                flag = True
                continue
            i += 1
        if flag == False:
            ans = "".join(my_list)
            print('#{} {}'.format(tc, ans), end='')
            # for i in my_list:
            #     print(i, end='')
            # print()


