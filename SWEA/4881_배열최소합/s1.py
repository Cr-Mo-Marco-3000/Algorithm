import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def mini(i, N):
    global total
    global min
    if i == N:
        # print(visited)
        if total <= min:
            min = total
        return
    elif total >= min:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                total += g[i][j]
                mini(i+1, N)
                visited[j] = 0
                total -= g[i][j]



for tc in range(1, T+1):
    # if tc >= 2:
    #     break
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min = 10 * N # 배열에는 이하의 자연수만 주어지므로 10 * N으로 초기화
    total = 0
    num_list = []
    mini(0, N)
    print(f'#{tc} {min}')


