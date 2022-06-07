import heapq

T = int(input())


def do():
    heap = []
    heapq.heappush(heap, (0, 0))
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            dist[v] = w
            for w in range(N+1):
                if not visited[w]:
                    heapq.heappush(heap, (dist[v] + g[v][w], w))
    return dist[N]


for tc in range(1, T+1):
    # 마지막 연결지점 번호 N과 도로의 개수 E가 주어진다.
    # 2. 빵디로 풀기
    N, E = map(int, input().split())
    g = [[20 for _ in range(N + 1)] for _ in range(N+1)]
    visited = [0] * (N+1)
    dist = [20] * (N+1)
    dist[0] = 0
    for _ in range(E):
        start, end, weight = map(int, input().split())
        g[start][end] = weight

    ans = do()
    print('#{} {}'.format(tc, ans))

