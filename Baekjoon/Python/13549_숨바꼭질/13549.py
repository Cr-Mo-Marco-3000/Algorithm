import sys, collections
input = sys.stdin.readline
N, K = map(int, input().strip().split())
visited = [1000000] * 100001
Q = collections.deque([(N, 0)])
length = len(visited)
while Q:
    v, time = Q.popleft()
    if 0 <= v < length and visited[v] > time:
        visited[v] = time
        Q.append((2*v, time))
        Q.append((v+1, time+1))
        Q.append((v-1, time+1))
print(visited[K])

# 문제 조건을 조금 잘못 읽고 꼬여서 헤맨 문제이다.
# 처음에는 재귀를 썼다가 시간 초과와 재귀초과가 떠서 bfs로 접근했는데
# 사실 답 구하는 느낌은 처음에 알았는데, visited를 비전형적으로 생각해서 여러 번 틀렸다.
# 처음에는 visited의 범위를 (2k+1)로 지정했다
# 문제에서 제시해주지는 않았지만 좌표의 최대값이 100,000인가보다.
# 이럴 때는 100,000을 넘어갔다 돌아오는 경우에 답이 다르게 나올 수 있다.
# 그 다음에는, visited의 범위를 k+1로 지정했는데
# 이 경우에는, 역시 좌표상으로 이동이 가능하지만 k값을 넘지 않는 경우에 문제가 생긴다.
# 사실 이동할 수 있는 범위를 제공해 주는 게 맞는 것 같다.