import sys
input = sys.stdin.readline

N = int(input())

my_list = []
for _ in range(N):
    my_list.append(int(input()))

cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if my_list[i] <= my_list[j]:
            break
        else:
            cnt += 1
print(cnt)

# 가장 먼저 생각난 풀이법이지만 시간 초과가 떴다.