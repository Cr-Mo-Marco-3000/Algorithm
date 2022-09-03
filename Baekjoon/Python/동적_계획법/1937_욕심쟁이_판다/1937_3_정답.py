import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)                                          # 재귀 깊이 설정
N = int(input().strip())
g = [list(map(int, input().strip().split())) for _ in range(N)]     
visited = [[0] * N for _ in range(N)]

def do(r, c):
    if not visited[r][c]:
        visited[r][c] = 1                                               # 미방문시 방문체크
        my_list = []                                                    # 네 방향 중 값을 넣기 위한 리스트
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N and g[nr][nc] > g[r][c]:     # 어차피 지나쳐 온 길은 자신보다 작으므로, 통과 불가
                my_list.append(do(nr, nc))                              # 네 방향을 체크해서 갈 수 있는 길들을 리스트에 넣음
        else:
            if my_list:                                                 # 만약 사방에 갈 수 있는 길이 있다면
                visited[r][c] = max(my_list) + 1                        # 갈 수 있는 길들 중 최대값 + 1이 현재 위치에서
            return visited[r][c]                                        # 갈 수 있는 최대 길이이므로 갱신
    else:
        return visited[r][c]                                            # 들어갔는데 이미 체크된 길이라면, 그 길에서 모든
                                                                        # 가능성이 체크 된 길이므로 그냥 그 값을 return

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ans = 0

for i in range(N):
    for j in range(N):
        do(i, j)
        if visited[i][j] > ans:                                         # i, j의 값은 이후 갱신될 가능성이 없으므로
            ans = visited[i][j]                                         # answer와 비교해서 확인해준다.

print(ans)

# 맨 처음에는, 순환하며 함수로 들어간 값들에만 memoization을 했는데, 역시나 시간초과가 떴다.
# 그 다음에 딥카피한 스택에 좌표를 저장해서 pop해가며 인자로 넣은 count로
# visited 값을 갱신해주다가
# 값만 깔끔하게 발라내서 쓰는 방법이 없을까 생각이 들어서 사방 탐색 중 값만 취했다.
# 역시 너무 어려운 방법은 이 정도 수준에서는 답이 아니다.
# 더 쉬운 방법은 언제나 존재한다.
