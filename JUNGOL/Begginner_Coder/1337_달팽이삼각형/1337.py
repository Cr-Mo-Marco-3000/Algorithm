from sys import stdin

N = int(stdin.readline().rstrip())

delta = ((1, 1), (0, -1), (-1, 0))

num = 0
r, c = 0, 0
g = [[-1] * N for _ in range(N)]

for _ in range(N):

while cnt:
    g[r][c] = num

    num = (num + 1) % 9
    r = delta[0]