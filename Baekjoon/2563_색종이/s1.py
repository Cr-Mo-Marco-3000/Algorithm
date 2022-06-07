import sys

sys.stdin = open('input.txt')

T = int(input())

g = [[0] * 101 for _ in range(101)]
a = [list(map(int, input().split())) for _ in range(T)]
total = 0

for i in range(T):
    for j in range(a[i][0], a[i][0] + 10):
        for k in range(a[i][1], a[i][1] + 10):
            if g[j][k] == 0:
                g[j][k] = 1
                total += 1
print(total)




    # print('#{} '.format(tc, ))

