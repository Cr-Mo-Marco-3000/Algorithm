import sys

sys.stdin = open('sample_input.txt')

arr = list(range(1, 13))


cnt = 0
T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N, K = map(int, input().split())
    for i in range(1 << 12):
        my_list = []
        for j in range(12):
            if i & (1 << j):
                my_list.append(arr[j])
        if len(my_list) == N and sum(my_list) == K:
            cnt += 1
    print(f'#{tc} {cnt}')