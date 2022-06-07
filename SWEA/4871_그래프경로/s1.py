import sys

sys.stdin = open('sample_input.txt')


def dfs(S, G):
    stack = [S]
    while stack:
        v = stack.pop()
        # 아래는 해답 판별조건, v가 G로 뽑혀나왔다는 이야기는, S부터 G까지 원사이드로 이어진다는 뜻이다.
        if v == G:
            return 1
        if not visited[v]:
            visited[v] = 1
            for w in range(V+1):
                if g[v][w] == 1 and not visited[w]:
                    stack.append(w)
    return 0                                            # 만약 G를 찾지 못하고 끝까지 순환했다면, 0을 반환


T = int(input())


for tc in range(1, T+1):
    # nod V, Edge E
    V, E = map(int, input().split())

    # temp_list
    temp = []
    for _ in range(E):
        temp.append(list(map(int, input().split())))

    # visited
    visited = [0] * (V + 1)

    # init graph
    g = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

    # 방향성 그래프이므로 행 => 열만 해 준다? 맞네
    for i in range(E):
        g[temp[i][0]][temp[i][1]] = 1
        # 아래 조건이 있다면, 양방향 그래프가 되어, 1에서 시작한 탐색이 4, 6, 3에서 끝나야 하는데, 3 => 2로 이어진다.
        # g[temp[i][1]][temp[i][0]] = 1

    # start nod: S, end nod: G
    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G)))