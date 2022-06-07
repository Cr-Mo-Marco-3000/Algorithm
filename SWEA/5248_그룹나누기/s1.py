import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def find_set(x):
    while arr[x] != x:
        x = arr[x]
    return x

# def union(x, y):

def union(y, x):
    arr[find_set(y)] = find_set(x)



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0]
    my_list = tuple(map(int, input().split()))
    for i in range(1, N+1):
        arr = arr + [i]
    for j in range(M):
        a = my_list[2*j]
        b = my_list[2*j + 1]
        union(a, b)
    my_set = set()
    print(arr)
    for k in arr:
        my_set.add(find_set(k))
    ans = len(my_set) - 1
    print('#{} {}'.format(tc, ans - 1))

