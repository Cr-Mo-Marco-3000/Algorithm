import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(r, elec, cnt):
    global ans
    if cnt == N-1:
        elec += g[r][0]
        if elec < ans:
            ans = elec
    for w in range(1, N):
        if not visited[w] and g[r][w]:
            visited[w] = 1
            # elec += g[r][w]
            do(w, elec '''+ g[r][w]''', cnt + 1)
            visited[w] = 0
            # elec -= g[r][w]


for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    ans = 10000000
    visited = [0] * N
    do(0, 0, 0)
    print('#{} {}'.format(tc, ans))

