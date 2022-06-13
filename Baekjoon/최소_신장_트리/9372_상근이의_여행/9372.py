import sys, heapq

input = sys.stdin.readline

T = int(input().strip())

def do():
    heap = []
    heapq.heappush(heap, 1)
    ans = 0
    while heap:
        v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            ans += 1
            for w in g[v]:
                if not visited[w]:
                    heapq.heappush(heap, w)
    return ans

for _ in range(T):
    N, M = map(int, input().strip().split())
    visited = [0] * (N + 1)
    g = [[] for _ in range(N + 1)]
    for i in range(M):
        start, end = map(int, input().strip().split())
        g[start].append(end)
        g[end].append(start)
    print(do()-1)


# 이 지랄맞은 최소신장트리랑 다익스트라는 언제쯤 기억에 남을 지 모르겠다
# 익숙해지겠다 하면 기억에서 사라지는 게 반복되니 원...
# 하지만 그래도 포기하지 않고 하다 보면 언젠가는 휘발성 높은 내 기억 속에서도 오래 남게 되지 않을까?