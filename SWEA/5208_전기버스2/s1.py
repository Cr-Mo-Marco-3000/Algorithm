import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(stop, cnt):
    global ans
    if stop >= N-1:
        if cnt < ans:
            ans = cnt
            return
    elif cnt >= ans:
        return
    else:
        for i in range(battery[stop], 0, -1):
            do(stop + i, cnt + 1)


for tc in range(1, T+1):
    my_list = list(map(int, input().split()))
    N = my_list[0]
    battery = my_list[1:]
    ans = N + 2
    do(0, 0)

    print('#{} {}'.format(tc, ans-1))

