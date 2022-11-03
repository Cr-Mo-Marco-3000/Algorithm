import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

my_list = list(map(int, input().strip().split()))

max_v = initial_v = sum(my_list[0:M])

for i in range(M, N):
    initial_v += (my_list[i] - my_list[i-M])
    if initial_v > max_v:
        max_v = initial_v

print(max_v)