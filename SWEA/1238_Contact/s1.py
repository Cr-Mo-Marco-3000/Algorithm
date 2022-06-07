import sys

sys.stdin = open('input.txt')

def do(S):
    Q = [S]
    visited[S] = 1
    while Q:
        v = Q.pop(0)
        for w in g[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)


T = 10

for tc in range(1, T+1):
    E, S = map(int, input().split())
    temp = list(map(int, input().split()))
    g = [[] for _ in range(max(temp) + 1)]
    for i in range(0, E//2):
        g[temp[2*i]].append(temp[2*i+1])
    visited = [0] * (max(temp) + 1)
    do(S)
    ans = 0
    max_v = max(visited)
    for j in range(len(visited) - 1, -1, -1):
        if visited[j] == max_v:
            ans = j
            break
    print(f'#{tc} {ans}')