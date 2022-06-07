import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str_1 = set(map(str, input()))
    str_2 = list(map(str, input()))
    str_1 = list(str_1)
    counts = []
    for i in str_1:
        counts.append(str_2.count(i))
    max_num = max(counts)
    print('#{} {}'.format(tc, max_num))

