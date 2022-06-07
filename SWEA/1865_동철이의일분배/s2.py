import sys

sys.stdin = open('input.txt')

T = int(input())

def do(cnt, perc):
    global ans
    if cnt == N:
        if perc > ans:
            ans = perc
    elif perc <= ans:
        return
    else:
        for w in range(N):
            if g[cnt][w] != 0:
                if not visited[w]:
                    visited[w] = 1
                    do(cnt + 1, perc * (g[cnt][w]) / 100)
                    visited[w] = 0




for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    do(0, 1)
    ans *= 100

    print('#{} {:.6f}'.format(tc, ans))

