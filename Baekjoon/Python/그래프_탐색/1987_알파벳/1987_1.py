import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
g = [list(map(str, input().strip())) for _ in range(N)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
visited = [[0] * M for _ in range(N)]
ans = 0
def do(r, c, cnt):
    global ans
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not my_dict[g[nr][nc]]:
            visited[nr][nc] = 1
            my_dict[g[nr][nc]] = 1
            do(nr, nc, cnt+1)
            visited[nr][nc] = 0
            my_dict[g[nr][nc]] = 0
    else:
        if ans < cnt:
            ans = cnt

my_dict = {}
for i in range(26):
    my_dict[f'{chr(65 + i)}'] = 0
visited[0][0] = 1
my_dict[g[0][0]] = 1
do(0, 0, 1)
print(ans)
