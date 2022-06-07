import sys
from collections import deque

sys.stdin = open('sample_input.txt')


def do(r, c):
    global ans
    sr = r
    sc = c
    for i in range(2, N):
        for j in range(1, i):
            left = j
            right = i - j
            for move in moves:
                r = sr
                c = sc
                eaten = set()
                seq = []
                seq += [move[0]] * left
                seq += [move[1]] * right
                seq += [move[2]] * left
                seq += [move[3]] * right
                k = 0
                eaten.add(g[r][c])
                while k < len(seq):
                    nr = r + dr[seq[k]]
                    nc = c + dc[seq[k]]
                    if 0 <= nr < N and 0 <= nc < N:
                        if g[nr][nc] not in eaten:
                            eaten.add(g[nr][nc])
                            r = nr
                            c = nc
                            k += 1
                        elif g[nr][nc] == g[sr][sc] and nr == sr and nc == sc:
                            if len(seq) > ans:
                                ans = len(seq)
                                # print(seq)
                            break
                        else:
                            break
                    else:
                        break


# 방향델타: 우상 우하 좌하 좌상
dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

# 이동 순서
moves = []
delta = deque([0, 1, 2, 3])
# delta_2 = deque([3, 2, 1, 0])
for i in range(4):
    delta.rotate(i)
    # delta_2.rotate(i)
    moves.append(list(delta))
    # moves.append(list(delta_2))
print(moves)

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(4):
        for j in range(4):
            do(i, j)

    print('#{} {}'.format(tc, ans))

