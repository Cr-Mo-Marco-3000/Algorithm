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
                    # 이거 안 해주고 걍 값을 넘겨주는 게 연산을 줄일 수 있고 편리하다
                    perc = perc * (g[cnt][w] / 100)
                    do(cnt + 1, perc)
                    perc = perc / (g[cnt][w] / 100)
                    visited[w] = 0


for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    # 연산을 줄일 수 있을 것 같은데, 첫 번째 일꾼이 0%의 가능성을 가질 때 문제가 된다
    # for i in range(N):
    #     ans *= g[i][0] / 100
    do(0, 1)
    ans *= 100

    print('#{} {:.6f}'.format(tc, ans))

