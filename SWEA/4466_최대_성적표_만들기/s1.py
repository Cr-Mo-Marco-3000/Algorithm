import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split())
    my_list = list(map(int, input().split()))
    max_value = 0
    my_list.sort(reverse=True)
    total = 0
    for i in range(K):
        total += my_list[i]

    # for i in range(1 << N):
    #     score_list = []
    #     for j in range(N):
    #         if i & (1 << j):
    #             score_list.append(my_list[j])
    #     if len(score_list) == K and sum(score_list) > max_value:
    #         max_value = sum(score_list)
    print('#{} {}'.format(tc, total))

