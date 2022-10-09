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
    for _ in range(V):
        min_idx = -1
        min_value = 12345
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1
        for j in range(V+1):
            if not visited[j] and g[min_idx][j] < key[j]:
                key[j] = g[min_idx][j]
    return sum(key)


import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
g = [[12345 for _ in range(V+1)] for _ in range(V+1)]

key = [12345] * (V+1)
key[0] = 0
visited = [0] * (V+1)

for i in range(E):
    start, end, W = map(int, input().split())
    g[start][end] = W
    g[end][start] = W

print(Prim())
