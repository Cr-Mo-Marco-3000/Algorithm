import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    int_2 = list(map(int, input()))
    int_3 = list(map(int, input()))
    for i in range(i, len(int_2)):
        int_2[i] = (int_2[i] + 1) % 2
        int_2[i] = (int_2[i] + 1) % 2

    print('#{} '.format(tc, ))

