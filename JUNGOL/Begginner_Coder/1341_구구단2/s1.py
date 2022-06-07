import sys

input = sys.stdin.readline

s, e = map(int, input().strip().split())

# 오름차순일 경우
if s <= e:
    for i in range(s, e+1):
        for j in range(1, 10):
            # 3, 6, 9일 경우
            if i * j // 10:
                blank = ""
            else:
                blank = " "
            if not j % 3:
                print(f'{i} * {j} = {blank}{i*j}')
            else:
                print(f'{i} * {j} = {blank}{i*j}   ', end="")
        print()

# 내림차순일 경우
else:
    for i in range(s, e-1, -1):
        for j in range(1, 10):
            # 3, 6, 9일 경우
            if i * j // 10:
                blank = ""
            else:
                blank = " "
            if not j % 3:
                print(f'{i} * {j} = {blank}{i * j}')
            else:
                print(f'{i} * {j} = {blank}{i * j}   ', end="")
        print()


# 앞에서 구구단 문제를 하나 풀어봐서 그런지, 다양한 조건을 생각하면서 풀어 실수를 하지 않을 수 있었다.