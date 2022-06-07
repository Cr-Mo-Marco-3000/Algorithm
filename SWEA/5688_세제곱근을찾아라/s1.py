import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    my_list = []
    ans = -1
    for i in range(0, 6):
        a = (10 ** i) ** 3
        b = (10 ** (i+1)) ** 3
        if a <= N < b:
            index = 10 ** i
            break
    for j in range(index, N+1):
        if j ** 3 == N:
            ans = j
        elif j ** 3 > N:
            break
    print('#{} {}'.format(tc, ans))
