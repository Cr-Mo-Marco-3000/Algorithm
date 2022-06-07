import sys

sys.stdin = open('input.txt')

T = int(input())
num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
key_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    tc_case = input()
    num_list = list(map(str, input().split()))
    for key in num_list:
        num_dict[key] += 1
    print('#{}'.format(tc))
    for key in key_list:
        print(f'{key} ' * num_dict[key], end="")
    print()
