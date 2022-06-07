import sys

sys.stdin = open('sample_input.txt')

T = int(input())
def do(i):
    global ans
    if i == N:
        ans += 1
        return
    else:
        for w in range(N):
            if not g[i][w]:
                g[i][w] = 1
                visited = []
                # 우하로 뻗기
                for j in range(N):
                    if 0 <= i + j < N and 0 <= w + j < N:
                        if not g[i + j][w + j]:
                            g[i + j][w + j] = 1
                            visited.append((i + j, w + j))
                    else:
                        break
                # 좌하로 뻗기
                for j in range(N):
                    if 0 <= i + j < N and 0 <= w - j < N:
                        if not g[i + j][w - j]:
                            g[i + j][w - j] = 1
                            visited.append((i + j, w - j))
                    else:
                        break
                # 아래로 뻗기
                for j in range(N):
                    if 0 <= i + j < N:
                        if not g[i + j][w]:
                            g[i + j][w] = 1
                            visited.append((i + j, w))
                    else:
                        break
            # 맞나 일케 하는거?
                do(i + 1)
                g[i][w] = 0
                while visited:
                    r, c = visited.pop()
                    g[r][c] = 0
        else:
            return
for tc in range(1, T+1):
    N = int(input())
    g = [[0] * N for _ in range(N)]
    ans = 0
    do(0)
    print('#{} {}'.format(tc, ans))

