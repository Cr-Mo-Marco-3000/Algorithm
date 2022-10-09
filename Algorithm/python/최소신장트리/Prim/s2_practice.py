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
    ans = 0                                             # ans 초기화
    heap = []                                           # 힙 리스트 초기화
    heapq.heappush(heap, (0, 0))                        # 힙에 시작 노드 추가(가중치, 노드번호), 둘 다 0
    while heap:
        w, v = heapq.heappop(heap)                      # w: 현재 가중치, v: 현재 정점 => 항상 최솟값 반환(최소힙 루트는 항상 최솟값)
        if not visited[v]:                              # 정점을 아직 방문 안했다면
            ans += w                                    # v까지 이동한 가중치 누적
            visited[v] = 1                              # 해당 정점을 방문하고, 선택해서 활용
            for n, weight in g[v]:                      # 인접 리스트에서 인접 정점
                if not visited[n]:                      # 그 정점을 아직 방문하지 않았다면
                    heapq.heappush(heap, (weight, n))   # v와 연결되어 있는 모든 (가중치, 인접 정점)을 추가
    return ans





import sys, heapq
sys.stdin = open('input.txt')


V, E = map(int, input().split())                        # V + 1개의 정점(0부터 시작)
visited = [0] * (V+1)                                   # 정점 방문 여부 체크
g = [[] for _ in range(V+1)]                            # 인접 리스트 구현

# 인접 리스트 구현
for _ in range(E):
    start, end, weight = map(int, input().split())      # 간선만큼(E) 돌면서 두 정점과 가중치를 받고 구현
    g[start].append([end, weight])                      # 무향 그래프 => (정점, 가중치) 형태로 추가
    g[end].append([start, weight])

print(Prim())