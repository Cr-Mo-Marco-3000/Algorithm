import sys

sys.stdin = open('input.txt')


def dfs():
    # 무조건 0부터 시작하므로, 넣고 시작한다.
    stack = [0]
    while len(stack):
        v = stack.pop()
        if v == 99:
            return 1
        if not visited[v]:
            visited[v] = 1
            # 0 부터 99까지 순환
            for w in range(100):
                if visited[w] == 0 and g[v][w]:
                    stack.append(w)
    return 0


T = 10

for _ in range(1, T+1):
    tc, E = map(int, input().split())
    
    # 요 넷은 세트로 묶어서 기억하는 게 나을 것 같다. 방문 리스트, 임시리스트, 그래프 초기화, 엣지 초기화
    visited = [0] * 100
    temp = list(map(int, input().split()))
    g = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(E):
        g[temp[2*i]][temp[2*i+1]] = 1
    # 무조건 0부터 시작하므로, 값을 받을 필요가 없다.
    ans = dfs()

    print('#{} {}'.format(tc, ans))
