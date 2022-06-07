import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    g =[[0,0,0] for _ in range(N +1)]
    temp = list(map(int, input().split()))
    for i in range(1, N+1):
        g[i][1] = temp[i-1]
        # 얘도 상관은 없음, 어차피 0의 값은 0이기 때문
        # while i != 0:
        while i != 1:
            if g[i][1] < g[i//2][1]:
                g[i][1], g[i//2][1] = g[i//2][1], g[i][1]
                # 짝수일 때는 필요 없고 홀수일 때 다시 한 번 비교
                # if i % 2:
                #     if g[i-1][1] < g[i//2][1]:
                #         g[i - 1][1], g[i // 2][1] = g[i//2][1], g[i-1][1]
            i = i//2
    cnt = 0
    j = N // 2
    while j != 0:
        cnt += g[j][1]
        j //= 2

    print('#{} {}'.format(tc, cnt))

