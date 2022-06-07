import sys
import copy
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = 9
    my_list = [list(map(int, input().split())) for _ in range(N)]
    nl = copy.deepcopy(my_list)
    reverse_list = list(map(list, zip(*my_list)))
    ans = 1
    for i in my_list:
        i.sort()

    for i in reverse_list:
        i.sort()

    for i in range(N-1):
        for j in range(N-1):
            if my_list[i][j] == my_list[i][j + 1]:
                ans = 0
                break
            if reverse_list[i][j] == reverse_list[i][j + 1]:
                ans = 0
                break
        if ans == 0:
            break

    start_list = [0, 3, 6]

    for i in start_list:
        for j in start_list:
            temp = []
            for k in range(3):
                for l in range(3):
                    temp.append(nl[i+k][j+l])
            temp.sort()
            for w in range(N-1):
                if temp[w] == temp[w+1]:
                    ans = 0
                    break
            if ans == 0:
                break
        if ans == 0:
            break
    print('#{} {}'.format(tc, ans))

