import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(cnt, money):
    global ans
    if cnt == N:
        if money < ans:
            ans = money
            return
    elif money >= ans:
        return
    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                do(cnt + 1, money + g[cnt][w])
                visited[w] = 0

for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 99 * N
    do(0, 0)
    print('#{} {}'.format(tc, ans))

