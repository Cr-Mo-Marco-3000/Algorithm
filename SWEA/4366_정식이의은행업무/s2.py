import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 1단계: 2진수를 10진수로 변경한다
# 2단계: %를 활용하여 이진수의 각 자리수가 1이면 0, 0이면 1로 만들어준다
# 리스트로 만들어서 각 자리별로 +1 해준 후 % 2 해주면 1은 0, 0은 1로 바뀐다.
# 3단계: 만들어준 새로운 수를 3진수로 변경한다.
# 4단계: 주어진 3진수의 각 자리수를 비교하며, 자리수가 하나만 다르다면 profit!

for tc in range(1, T+1):
    # bin_num = input()
    # tri_num = input()
    # dec_num = 0
    # for i in range(len(bin_num)):
    #     dec_num += int(bin_num[i]) * 2 ** (len(bin_num) - 1 - i)
    # for j in range(len(bin_num) - 1):
    #     if dec_num & (1 << j):
    #         dec_num -= 2 ** j
    #         temp = dec_num
    #         # 3진수 변경
    #         num_3 = ''
    #         while temp:
    #             num_3 = str(temp % 3) + num_3
    #             temp //= 3
    #         cnt = 0
    #         if len(num_3) == len(tri_num):
    #             for k in range(len(num_3)):
    #                 if tri_num[k] != num_3[k]:
    #                     cnt += 1
    #             if cnt == 1:
    #                 break
    #         dec_num += 2 ** j
    #     elif not (dec_num & (1 << j)):
    #         dec_num += 2 ** j
    #         temp = dec_num
    #         # 3진수 변경
    #         num_3 = ''
    #         while temp:
    #             num_3 = str(temp % 3) + num_3
    #             temp //= 3
    #         cnt = 0
    #         if len(num_3) == len(tri_num):
    #             for k in range(len(num_3)):
    #                 if tri_num[k] != num_3[k]:
    #                     cnt += 1
    #             if cnt == 1:
    #                 break
    #         dec_num -= 2 ** j
    # print('#{} {}'.format(tc, dec_num))

