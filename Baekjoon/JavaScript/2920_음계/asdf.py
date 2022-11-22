import sys
input = sys.stdin.readline

N = int(input().strip())
my_list = [0] * 10001
for i in range(N):
    my_list[int(input().strip())] += 1

for j in range(10001):
    if (my_list[j]):
        while my_list[j]:
            my_list[j] -= 1
            print(j)