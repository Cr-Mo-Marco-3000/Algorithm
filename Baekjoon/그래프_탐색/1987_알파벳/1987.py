# pypy로는 정답
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split()) 
def do(r, c, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not alpha[g[nr][nc]]:
            visited[nr][nc] = 1
            alpha[g[nr][nc]] = 1
            do(nr, nc, cnt+1)
            visited[nr][nc] = 0
            alpha[g[nr][nc]] = 0


g = [list(map(ord, input().strip())) for _ in range(N)] # 문자열은 처리하기 힘들기 때문에, 숫자로 바꾸어준다.
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
alpha = [0] * 91 # count 배열같이, 각 알파벳을 숫자로 바꾸어 주었으므로 이미 쓴 알파벳인지를 평가
visited = [[0] * M for _ in range(N)] 
alpha[g[0][0]] = 1 # 0,0은 방문처리
visited[0][0] = 1 # 0,0은 방문처리
ans = 0
do(0,0,1)
print(ans)
