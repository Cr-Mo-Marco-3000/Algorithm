import sys

sys.stdin = open('input.txt')

T = 10


for _ in range(1, T+1):
    tc = int(input())
    ml = list(map(int, input().split()))
    while ml[-1] > 0:
        ml.append(ml.pop(0) - 1)
        if ml[-1] <= 0:
            ml[-1] = 0
            break
        ml.append(ml.pop(0) - 2)
        if ml[-1] <= 0:
            ml[-1] = 0
            break
        ml.append(ml.pop(0) - 3)
        if ml[-1] <= 0:
            ml[-1] = 0
            break
        ml.append(ml.pop(0) - 4)
        if ml[-1] <= 0:
            ml[-1] = 0
            break
        ml.append(ml.pop(0) - 5)
        if ml[-1] <= 0:
            ml[-1] = 0
            break
    print('#{} '.format(tc), end='')
    print(*ml)

