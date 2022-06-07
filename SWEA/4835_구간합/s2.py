import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 정수의 개수 N, 구간의 넓이 M
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    v = 0
    for i in range(0, 3):
        v += my_list[i]

    max_v = min_v = v
    j = 0

    while j < N - M:
        v = v - my_list[j] + my_list[j+M]
        if v > max_v:
            max_v = v
        if v < min_v:
            min_v = v
        j += 1
    print(f'#{tc} {max_v - min_v}')
