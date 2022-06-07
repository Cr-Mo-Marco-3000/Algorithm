import sys, heapq

sys.stdin = open('sample_input.txt')

T = int(input())

def do():
    heap = []
    heapq.heappush(heap, (0, 0))
    ans = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            ans += w
            for nod, weight in g[v]:
                if not visited[nod]:
                    heapq.heappush(heap, (weight, nod))

    return ans


for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        g[start].append((end, weight))
        g[end].append((start, weight))
    visited = [0] * (V+1)
    ans = do()
    print('#{} {}'.format(tc, ans))

