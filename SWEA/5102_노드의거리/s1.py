import sys

sys.stdin = open('sample_input.txt')

def do(S):
    visited[S] = 1
    Q = [S]
    while Q:
        v = Q.pop(0)
        if v == G:
            return visited[v]
        for w in range(1, V+1):
            if not visited[w] and w in g[v]:
                visited[w] = visited[v] + 1
                Q.append(w)
    return 1


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    # 아바바 아바바바바바
    print(f'#{tc} {do(S) - 1}')
    


