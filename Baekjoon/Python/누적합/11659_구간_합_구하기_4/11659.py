import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

my_list = list(map(int, input().strip().split()))

for i in range(1, N):
    my_list[i] = my_list[i] + my_list[i-1]

for _ in range(M):
    start, end = map(int, input().strip().split())
    if start == 1:
        print(my_list[end-1])
    else:
        print(my_list[end-1]-my_list[start-2])
