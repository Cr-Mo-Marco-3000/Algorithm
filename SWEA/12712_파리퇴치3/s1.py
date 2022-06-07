import sys

sys.stdin = open('in1.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    # 방향 델타 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 방향 델타 우상, 우하, 하좌, 좌상
    dr2 = [-1, 1, 1, -1]
    dc2 = [1, 1, -1, -1]
    # 중심값 정하기
    max_v = 0
    for i in range(N):
        for j in range(N):
            val_x = g[i][j]
            val_c = g[i][j]
            for k in range(4): # 방향델타 순서
                for l in range(1, M):
                    nr, nc = i + (dr[k] * l), j + (dc[k] * l)
                    if 0 <= nr < N and 0 <= nc < N:
                        val_c += g[nr][nc]
                    nr, nc = i + (dr2[k] * l), j + (dc2[k] * l)
                    if 0 <= nr < N and 0 <= nc < N:
                        val_x += g[nr][nc]
            total = max(val_c, val_x)
            if max_v < total:
                max_v = total
    # 스프레이 뿌리기
    print('#{} {}'.format(tc, max_v))

