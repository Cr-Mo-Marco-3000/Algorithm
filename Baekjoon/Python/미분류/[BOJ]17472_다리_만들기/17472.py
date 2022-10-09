import sys, collections, heapq

input = sys.stdin.readline

N, M = map(int, input().strip().split())

g = [list(map(int, input().strip().split())) for _ in range(N)]
cnt = 1

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 1단계, 다리별로 나눔
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if g[i][j] and not visited[i][j]:
            Q = collections.deque([(i, j)])
            g[i][j] = cnt
            visited[i][j] = 1
            while Q:
                r, c = Q.popleft()
                for w in range(4):
                    nr = r + dr[w]
                    nc = c + dc[w]
                    if 0 <= nr < N and 0 <= nc < M and g[nr][nc] and not visited[nr][nc]:
                        g[nr][nc] = cnt
                        visited[nr][nc] = 1
                        Q.append((nr, nc))
            else:
                cnt += 1

# 각 다리에서 뻗어서 닿는지 검사
g2 = [[12] * (cnt) for _ in range(cnt)]
visited_2 = [0] * (cnt)
for i in range(N):
    for j in range(M):
        if g[i][j]:
            island_number_1 = g[i][j]
            for w in range(4):
                ni = i + dr[w]
                nj = j + dc[w]
                # 사방 탐색 중 0 발견
                if 0 <= ni < N and 0 <= nj < M and not g[ni][nj]:
                    bridge = 1
                    while 0 <= ni < N and 0 <= nj < M:
                        ni = ni + dr[w]
                        nj = nj + dc[w]
                        if 0 <= ni < N and 0 <= nj < M and g[ni][nj]:
                            if bridge < g2[island_number_1][g[ni][nj]] and bridge >= 2:
                                g2[island_number_1][g[ni][nj]], g2[g[ni][nj]][island_number_1] = bridge, bridge
                                break
                            else:
                                break
                        bridge += 1

# g2가지고 최소 신장 트리 => 맨날 까먹음...
ans = 0
heap = []
heapq.heappush(heap, (0, 1))
while heap:
    dist, v = heapq.heappop(heap)
    if not visited_2[v]:
        ans += dist
        visited_2[v] = 1
        for w in range(1, cnt):
            if g2[v][w] != 12 and not visited_2[w]:
                heapq.heappush(heap, (g2[v][w], w))

for s in range(1, cnt):
    if not visited_2[s]:
        print(-1)
        break
else:
    print(ans)