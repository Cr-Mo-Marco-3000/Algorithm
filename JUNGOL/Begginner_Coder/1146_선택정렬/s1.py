import sys
input = sys.stdin.readline

N = int(input().rstrip())
my_list = list(map(int, input().rstrip().split()))

for i in range(N-1):
    min_idx = i
    min_value = my_list[i]
    for j in range(i+1, N):
        if my_list[j] < min_value:
            min_idx = j
            min_value = my_list[j]
    my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    print(*my_list)

# 오랜만에 선택정렬을 하니까 헷갈린다.
# 특히 마지막 인덱스 부분을 정할 때 나도 모르게 -1을 하고 말았다.