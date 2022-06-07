import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    gr = [[0 for _ in range(10)] for _ in range(10)]
    total = 0
    N = int(input())
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if gr[i][j] == 0 or gr[i][j] == 2:
                        gr[i][j] += 1
                    if gr[i][j] == 3:
                        total += 1

        elif color == 2:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if gr[i][j] == 0 or gr[i][j] == 1:
                        gr[i][j] += 2
                    if gr[i][j] == 3:
                        total += 1
    print('#{} {}'.format(tc, total))

