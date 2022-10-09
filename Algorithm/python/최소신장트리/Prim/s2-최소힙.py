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

def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, 0))                        # item의 순서 -> (가중치, 정점)
    while heap:
        w, v = heapq.heappop(heap)                      # w: 현재 가중치 / v: 현재 정점 -> 항상 최솟값이 반환 (최소힙의 루트는 항상 최솟값)
        if not visited[v]:                              # 정점을 아직 방문 안했다면
            ans += w                                    # v까지 이동한 가중치 누적
            visited[v] = 1                              # 해당 정점 선택하여 활용
            for w, weight in G[v]:                      # 인접 리스트에서 인접 정점(w)과 가중치(weight)를 가져와서
                if not visited[w]:                      # 그 정점(w)을 아직 체크 안했다면
                    heapq.heappush(heap, (weight, w))   # v와 연결되어 있는 모든 (가중치 + 인접 정점)을 추가
    return ans

import sys
import heapq
sys.stdin = open('input.txt')
V, E = map(int, input().split())                        # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1이 된다는 점 유의
G = [[] for _ in range(V+1)]                            # 인접 리스트
ans = 0                                                 # 누적 할 가중치
visited = [0] * (V+1)                                   # 정점의 선택 여부 체크
for i in range(E):
    start, end, W = map(int, input().split())           # 간선만큼 돌면서 두 정점과 가중치를 받고 인접 리스트 구현
    G[start].append([end, W])                           # 무방향 그래프 -> (정점, 가중치) 형태로 추가
    G[end].append([start, W])
print(prim())                                           # 22