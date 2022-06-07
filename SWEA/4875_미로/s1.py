import sys

sys.stdin = open('sample_input.txt')


def dfs(r, c):
    global ans
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 4 벽 체크
        if 0 <= nr < N and 0 <= nc < N:
            # 만약 이동한 곳이 도착 지점이라면
            if data[nr][nc] == 3:
                # 끝내자
                ans = 1
                return
            # 갈 수 있는 곳? => 통로 / 방문 했는지
            if data[nr][nc] == 0 and not visited[nr][nc]:
                dfs(nr, nc)






T = int(input())

# 방향 델타 생성: 상 0 우 1  하 2  좌 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


for tc in range(1, T+1):
    # 가로 세로 길이 N
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0
    # 1. 출발지 좌표 찾기
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                # 2. 출발지에서 탐색 시작
                dfs(r, c)


    print('#{} {}'.format(tc, ans))

