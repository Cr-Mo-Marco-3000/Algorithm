import sys

sys.stdin = open('input.txt')

T = int(input())




def do(p_list):



# core의 개수는 1 <= 12
for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    p_list = []
    # 상하좌우 방향델타
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # porcessor_list에 좌표를 저장
    for i in range(N):
        for j in range(N):
            if g[i][j] == 1:
                p_list.append([i,j])
    K = len(p_list)


    # print('#{} '.format(tc, ))

