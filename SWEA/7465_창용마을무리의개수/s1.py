import sys

sys.stdin = open('s_input.txt')

T = int(input())

def find(x):
    while x != arr[x]:
        x = arr[x]
    return x

def union(x, y):
    arr[find(y)] = arr[find(x)]



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0]
    for i in range(1,N+1):
        arr += [i]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    my_set = set()
    for i in range(1, N + 1):
        my_set.add(find(i))
    ans = len(my_set)

    print('#{} {}'.format(tc, ans))

