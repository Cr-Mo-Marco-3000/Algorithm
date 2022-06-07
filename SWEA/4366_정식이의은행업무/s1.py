import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do2():
    # str_3: 212 # int_3: 23
    global int_3
    global ans
    for k in range(len_3-1, -1, -1):
        int_3 -= int(str_3[k]) * 3 ** (len_3 - 1 - k)
        for l in range(3):
            if l != int(str_3[k]):
                int_3 += l * 3 ** (len_3 - 1 - k)
                if int_3 == int_2:
                    return int_3
                int_3 -= l * 3 ** (len_3 - 1 - k)
        int_3 += int(str_3[k]) * 3 ** (len_3 - 1 - k)




def do():
    global int_2
    for i in range(len_2):
        if int_2 & (1 << i):
            int_2 -= 2 ** i
            if int_2 == do2():
                return int_2
            int_2 += 2 ** i
        elif not int_2 & (1 << i):
            int_2 += 2 ** i
            # do2()
            if int_2 == do2():
                return int_2
            int_2 -= 2 ** i


for tc in range(1, T+1):
    num_2 = input()
    len_2 = len(num_2)
    num_3 = input()
    str_3 = num_3
    len_3 = len(num_3)
    num_2 = int(num_2)
    int_2 = 0
    num_3 = int(num_3)
    int_3 = 0
    ans = 0
    # 각각 10진수로 변환
    i = 0
    while num_2 > 0:
        int_2 += (num_2 % 10) * (2 ** i)
        num_2 //= 10
        i += 1
    # print(int_2)
    j = 0
    while num_3 > 0:
        int_3 += (num_3 % 10) * (3 ** j)
        num_3 //= 10
        j += 1
    # print(int_3)
    # print(int(str[1])
    ans = do()


    print('#{} {}'.format(tc, ans))

