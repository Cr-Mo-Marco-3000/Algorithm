import sys

input = sys.stdin.readline


def do(v, w):
    global min_v
    if w >= min_v:                      # 중간에 비용이 이미 지정된 최소비용을 넘어버리면 더 볼 필요가 없다.
        return
    if not (0 in visited):              # 이 부분을 더 낫게 고칠 수 있을 것 같은데
        if not g[v][0]:                 # count등을 변수로 따로 받아 주는 게 더 나을 수도 있겠다.
            return                      # 모든 지점을 방문한 상태에서, 마지막에 위치한 곳에 회사로 가는 길이 없으면 리턴
        else:
            if w + g[v][0] < min_v:     # 회사로 가는 길이 있다면, 그곳에서 회사로 가는 비용을 더하는 게 최소비용보다 작으면 갱신
                min_v = w + g[v][0]
                return
            else:
                return
    else:
        for t in range(N):
            if not visited[t] and g[v][t]:
                visited[t] = 1
                do(t, w + g[v][t])
                visited[t] = 0


N = int(input().strip())

visited = [0] * N

min_v = 99 * N              # 문제에서 주어진 대로 min_v를 준다.

g = [tuple(map(int, input().strip().split())) for _ in range(N)]

visited[0] = 1              # 중간에 회사로 돌아오는 게 아니므로, 미리 방문 체크를 하고 마지막에 따로 계산한다.

do(0, 0)                    # 출발은 회사로부터 시작하니까 0부터 시작

print(min_v)