import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    leng = int(input())
    num_list = input()
    counts = [0] * 10
    for i in num_list:
        counts[int(i)] += 1
    max_card = 0
    max_card_num = 0
    for j in range(len(counts)):
        if counts[j] >= max_card_num:
            max_card = j
            max_card_num = counts[j]

    print('#{} {} {}'.format(tc, max_card, max_card_num))

