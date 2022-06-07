import sys

sys.stdin = open('input.txt')

T = int(input())

def do(stone):
    # 흑돌 1 백돌 2
    # x,y 좌표가 바뀌어서 들어온다. 주의할것
    c, r, s = stone
    if s == 1:
        g[r][c] = 1
        # 8방 검사
        for w in range(8):
            nr = r + dr[w]
            nc = c + dc[w]
            # 검사중인 방향에 색이 다른 돌이 있을 경우
            if 1 <= nr <= N and 1 <= nc <= N and g[nr][nc] == 2:
                # 뻗어나가며 검사
                for j in range(N):
                    k = nr + dr[w] * j
                    l = nc + dc[w] * j
                    # 만약 다시 같은 색의 돌을 만나면
                    if 1 <= k <= N and 1 <= l <= N and g[k][l] == 1:
                        for n in range(0, j):
                            # 중간 돌들의 색을 변경하고
                            g[nr + dr[w] * n][nc + dc[w] * n] = 1
                        # 이걸 해줘야 한다!!! 해주지 않으면, 계속 뻗어나가며 과변경을 할 수 있다.
                        # 만약 1 2 1 2 1 이런 식으로 있는 경우, 중간에 1을 만나서 1 1 1 2 1이 되어야 하는데
                        # 끝까지 가면서 1 1 1 1 1 로 변경할 수 있다.
                        break
                    # 중간에 0을 만나서 끊기는 경우도 체크해주여야 한다.
                    elif 1 <= k <= N and 1 <= l <= N and g[k][l] == 0:
                        break
    if s == 2:
        g[r][c] = 2
        # 8방 검사
        for w in range(8):
            nr = r + dr[w]
            nc = c + dc[w]
            # 방향에 서로 다른 돌이 있을 경우
            if 1 <= nr <= N and 1 <= nc <= N and g[nr][nc] == 1:
                # 뻗어나가며 검사
                for j in range(N):
                    k = nr + dr[w] * j
                    l = nc + dc[w] * j
                    if 1 <= k <= N and 1 <= l <= N and g[k][l] == 2:
                        for n in range(0, j):
                            g[nr + dr[w] * n][nc + dc[w] * n] = 2
                        break
                    elif 1 <= k <= N and 1 <= l <= N and g[k][l] == 0:
                        break





for tc in range(1, T+1):
    # 변의 길이 N, 돌 놓는 횟수 M
    N, M = map(int, input().split())
    # 그래프 초기화
    g = [[0] * (N+1) for _ in range(N+1)]
    g[N//2][N//2] = 2
    g[N//2 + 1][N//2] = 1
    g[N//2][N//2 + 1] = 1
    g[N//2 + 1][N//2 + 1] = 2
    my_list = []
    # 상 우 하 좌, 우상, 우하, 좌하 좌상
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]
    for _ in range(M):
        my_list.append(list(map(int, input().split())))
    # 0, 1, 2
    for i in range(len(my_list)):
        do(my_list[i])

    
    # 계산하기
    ans = [0, 0]
    for x in range(1, N+1):
        for y in range(1, N+1):
            if g[x][y] == 1:
                ans[0] += 1
            elif g[x][y] == 2:
                ans[1] += 1
    print(f'#{tc} {ans[0]} {ans[1]}')
    # 흑돌 1 백돌 2