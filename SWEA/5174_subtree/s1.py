import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(N):
    global cnt
    if N != 0:
    # if N:             # 얘도 가능
        cnt += 1
        do(g[N][0])
        do(g[N][1])


# def do(N):
#     global cnt
#     if g[N]:
#         cnt += 1
#         if g[N][0] != 0:
#             do(g[N][0])
#         if g[N][1] != 0:
#             do(g[N][1])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    g = [[0, 0, 0] for _ in range(0, E + 2)]
    temp = list(map(int, input().split()))
    for i in range(E):
        if g[temp[2*i]][0] == 0:
            g[temp[2*i]][0] = temp[2*i + 1]
        else:
            g[temp[2*i]][1] = temp[2 * i + 1]
        g[temp[2*i+1]][2] = temp[2*i]
    cnt = 0
    do(N)
    print('#{} {}'.format(tc, cnt))

