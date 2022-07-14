import sys, collections

input = sys.stdin.readline

N, M = map(int, input().strip().split())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ice_list = []                                                   # 얼음 좌표와 얼음의 양 리스트
g = [list(map(int, input().strip.split())) for _ in range(N)]   # 그래프

# bfs 시작 지점 잡아주기
start_point = 0
for i in range(N):
    for j in range(M):
        if g[i][j]:
            start_point = (i, j)
            break
    if start_point:
        break
