import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int,input().split()))
    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):

    print('#{} '.format(tc, ))
i = 0
while i < len(my_string_list) - 1:
    my_string[i+1] >= my_sting[i]