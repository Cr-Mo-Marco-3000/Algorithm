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

크루스칼
 - 간선 중심
 - 간선을 오름차순 정렬 & 간선 개수만큼 선택
 - union & find 활용하여 사이클 생성 방지
"""

def make_set(x):
    """
    유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    """
    p[x] = x                     # 노드 x의 부모 저장

def find_set(x):
    """
    x를 포함하는 집합을 찾는 연산
    """
    if p[x] != x:                # x가 루트가 아닌 경우
        p[x] = find_set(p[x])    # 다시 루트 찾아서 재귀 호출
    return p[x]                  # x의 대표값 반환

def union(x, y):
    """
    x와 y를 포함하는 두 집합을 통합하는 연산
    """
    p[find_set(y)] = find_set(x) # y의 대표자를 x의 대표자로 변경


def kruskal():
    global ans
    edge_cnt = idx = 0                       # ans(최종 가중치 누적값) / edge_cnt(간선 선택 개수 -> V개 선택) / idx (간선 정보를 컨트롤을 위한 제어 변수)

    while edge_cnt != V:                     # 선택한 간선의 수(edge_cnt)가 전체 정점의 수(V)와 같아지기 전까지(신장 트리 조건)
        x = edges[idx][0]                    # 간선 정보에서 두 정점을 찾아
        y = edges[idx][1]
                                             # 두 점의 대표 원소 비교 (대표 원소가 다르면 같은 집합 아니고 같으면 같은 집합이기 때문에 사이클 형성)
        if find_set(x) != find_set(y):       # 같은 그룹이 아닐 때만 (사이클 방지)
            union(x, y)                      # union
            edge_cnt += 1                    # union을 한 것은 간선을 선택 한 것을 의미하니 edge_cnt를 증가
            ans += edges[idx][2]             # 해당 간선의 가중치를 누적하자
        idx += 1                             # 위의 조건문에 관계없이 다음 간선을 선택하기 위해 idx를 증가
                                             # 사이클이 생겨 뛰어넘는 경우 if 조건문을 타지 않으니 다음 간선 선택을 위해 idx는 어떤 경우에도 증가 필요

import sys
sys.stdin = open('input.txt')
ans = 0
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]  # 간선 정보
p = [0] * (V+1)                                              # 상호배타집합에 활용 할 노드 정보 (인덱스를 맞춰주기 위해 V+1)
edges = sorted(edges, key=lambda x: x[2])                    # 가중치(인덱스 2번)를 기준으로 정렬

"""
edges = []
for _ in range(E):
    n1, n2, w = map(int, input().split())
    edges.append((w, n1, n2))
edges.sort()
"""

# p = list(range(V+1))
for i in range(V+1):
    make_set(i)
kruskal()
print(ans)                                                   # 22