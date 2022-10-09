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
"""

def Prim():
    for _ in range(V):                      # 모든 정점이 MST에 포함될 때 까지 반복(마지막 요소 선택 여부)
        min_weight = 12345                  # 답을 sum(key)로 구하기 때문에 노드 개수만큼 반복할 필요 없다.
        min_index = -1                      

        # 1. MST에 연결된 노드들 중 최소 가중치 찾기
        for i in range(V+1):
            if not visited[i] and key[i] < min_weight:      # 아직 MST에 포함되지 않은 노드들 중 최소 비용 간선 찾기
                min_weight = key[i]                         
                min_index = i
        visited[min_index] = 1                              # 최소 비용 간선을 택해 그 노드를 체크

        # 2. 해당 값으로부터 연결된 정점 가중치 갱신
        for j in range(V+1):                                # min_index와 연결된 인접 행열 순환하며
            if not visited[j] and g[min_index][j] < key[j]: # 미선택 노드고 가중치가 기존 key의 가중치보다 작으면
                key[j] = g[min_index][j]                    # 즉 더 저렴하게 갈 수 있으면 갱신

    print(key)
    return sum(key)



import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())                            # 0부터 시작해서 V까지 V+1개의 정점

g = [[12345 for _ in range(V+1)] for _ in range(12345)]     # 그래프는 임의의 큰 값을 잡고 초기화(최소 신장 트리이므로)

visited = [0] * (V+1)                                       # 노드의 MST 포함 여부를 체크하기 위한 배열
key = [12345] * (V+1)                                       # MST 외부 노드들로의 간선들 중 최소 가중치 간선을 판단하기 위한 배열
key[0] = 0                                                  # 시작점 설정(시작점은 가중치가 0이므로)

for _ in range(E):                                          # 무향 그래프이므로 양쪽에 모두 가중치를 줌
    start, end, weight = map(int, input().split())
    g[start][end] = weight
    g[end][start] = weight

print(Prim())