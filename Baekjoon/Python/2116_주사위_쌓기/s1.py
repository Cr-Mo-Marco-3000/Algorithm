import sys
import copy
sys.stdin = open('input.txt')

T = int(input())



# idx 0:5 , 1:3, 2:4
my_list = [list(map(int, input().split())) for _ in range(T)]
total_list = []
total = 0
for a in range(6):
    total = 0
    new_list = copy.deepcopy(my_list)
    i = 0
    while i < T:
        if a == 0:
            b = 5
        elif a == 1:
            b = 3
        elif a == 2:
            b = 4
        elif a == 3:
            b = 1
        elif a == 4:
            b = 2
        elif a == 5:
            b = 0
        bot = new_list[i][a]
        top = new_list[i][b]
        new_list[i].remove(bot)
        new_list[i].remove(top)
        i += 1
        if i < T:
            a = new_list[i].index(top)
    for j in new_list:
        total += max(j)
    total_list.append(total)


print(max(total_list))