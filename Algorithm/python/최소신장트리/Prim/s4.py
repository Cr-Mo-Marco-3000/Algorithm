"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합

heap 활용하면 최솟값을 찾는 과정 생략 가능
 - min_heap을 구하면 root는 항상 최소 가중치 위치
 - heap_pop을 할 때마다 root에 있는 최소 가중치 반환
"""

def Prim():
    heap = [(0, 0)]
    total = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = 1
            total += w
            for n, w in g[v]:
                if not visited[n]:
                    heapq.heappush(heap, (w, n))
    return total

import sys
sys.stdin = open('input.txt')
import heapq

V, E = map(int, input().split())
g = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(V+1):
    start, end, w = map(int, input().split())
    g[start].append((end, w))
    g[end].append((start, w))

print(Prim())