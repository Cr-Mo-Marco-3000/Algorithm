T = int(input())


def do(r, c, flag, cnt):
    global max_v
    if not visited[r][c]:
        visited[r][c] = 1
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N:
            if g[nr][nc] < g[r][c] and not visited[nr][nc]:
                do(nr, nc, flag, cnt + 1)
                visited[nr][nc] = 0
            elif g[nr][nc] >= g[r][c] and not visited[nr][nc] and flag == 1:
                for k in range(1, K + 1):
                    g[nr][nc] -= k
                    if g[nr][nc] < g[r][c]:
                        do(nr, nc, 0, cnt + 1)
                        visited[nr][nc] = 0
                        flag = 1
                    g[nr][nc] += k
    else:
        if cnt > max_v:
            max_v = cnt


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 방향델타: 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    g = []
    max_height = 0
    max_list = []

    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(len(temp)):
            if temp[j] > max_height:
                max_list = [[i, j]]
                max_height = temp[j]
            elif temp[j] == max_height:
                max_list.append([i, j])
        g.append(temp)

    visited = [[0] * N for _ in range(N)]
    max_v = 0

    for p in max_list:
        do(p[0], p[1], 1, 1)
        visited[p[0]][p[1]] = 0

    print(f'#{tc} {max_v}')
