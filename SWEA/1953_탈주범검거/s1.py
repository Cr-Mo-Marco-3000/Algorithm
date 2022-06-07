import sys


sys.stdin = open('sample_input.txt')


def connect(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


def do(r, c):
    global cnt
    visited[r][c] = 1
    cnt += 1
    Q = [[r, c]]
    while Q:
        v = Q.pop(0)
        r, c = v[0], v[1]
        for w in range(4):
            if pipe[g[r][c]][w]:
                nr = r + dr[w]
                nc = c + dc[w]
                movable = connect(w)
                if 0 <= nr < N and 0 <= nc < M:
                    if pipe[g[nr][nc]][movable] and not visited[nr][nc]:
                        if visited[r][c] + 1 <= L:
                            visited[nr][nc] = visited[r][c] + 1
                            Q.append([nr, nc])
                            cnt += 1


T = int(input())


for tc in range(1, T+1):
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L

    N, M, R, C, L = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0,0,1,1], [1, 0, 0, 1]]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    do(R, C)
    print(f'#{tc} {cnt}')