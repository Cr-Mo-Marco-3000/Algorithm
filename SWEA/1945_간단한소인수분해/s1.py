import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    limit_a = 0 # 완전탐색으로 한다고 해도, 제약을 걸어야 하는데
    limit_c = 0 # 한 수를 제곱해 나갔을 때, N보다 커지는 순간을 리미트로 삼아,
    limit_d = 0 # 그 리미트보다 작은 범위에서 탐색한다.
    limit_e = 0
    # 부분집합문제와 비슷한 느낌이 들었는데... 느낌만인가 보다.

    while N > 2 ** limit_a:
        limit_a += 1

    limit_b = limit_a # 어차피 2의 제한보다는,
    while N < 3 ** limit_b: # b의 제한이 작되 그리 큰 차이는 나지 않을 테니, a의 제한에서 빼주는 식으로 나간다.
        limit_b -= 1
    limit_b += 1 # limit를 a와 맞추기 위해 +1을 해 준다.

    limit_c = limit_b
    while N < 5 ** limit_c:
        limit_c -= 1
    limit_c += 1

    limit_d = limit_c
    while N < 7 ** limit_d:
        limit_d -= 1
    limit_d += 1

    limit_e = limit_d
    while N < 11 ** limit_e:
        limit_e -= 1
    limit_e += 1

    my_list = []
    # 5중 for문을 돌아본다.
    for a in range(limit_a):
        for b in range(limit_b):
            for c in range(limit_c):
                for d in range(limit_d):
                    for e in range(limit_e):
                        my_list.append([a, b, c, d, e])
    for i in my_list:
        if N == (2 ** i[0]) * (3 ** i[1]) * (5 ** i[2]) * (7 ** i[3]) * (11 ** i[4]):
            print('#{} {} {} {} {} {}'.format(tc, i[0], i[1], i[2], i[3], i[4   ]))




