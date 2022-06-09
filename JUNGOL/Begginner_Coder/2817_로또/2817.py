import sys

input = sys.stdin.readline

def do(cnt, start):
    if cnt == 6:
        print(*lotto)
        return
    else:
        for w in range(start, K):
            lotto[cnt] = my_list[w]
            do(cnt + 1, w + 1)

K, *my_list = map(int, input().strip().split())

my_list = list(my_list)
lotto = [0] * 6

do(0, 0)