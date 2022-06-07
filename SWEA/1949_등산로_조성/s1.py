import sys

sys.stdin = open('input.txt')

# 해치웠나?
T = int(input())

# 1. visited를 갖고 가는 게 낫겠다.
# max 값을 가지고 다녀야 하는구나...

# => 응 둘 다 필요 없어

def do(r, c, flag):
    global max_v
    '''
    좌표 r, c
    등산로 길이 cnt,
    깎은 여부 플래그 flag
    
    visited 수복 해 줘야 할 것 같은데...
    g도 가져가야 될 것 같은데...
    응 둘 다 가져가도 어차피 무용지물이야.
    
    => 리스트를 가져가면, 새로운 리스트가 만들어지는 게 아니라 기존 리스트를 계속 사용하기 때문에
    => 리스트를 계속 가져가는 건 무용지물이고, 백트래킹을 써야 한다.
    '''
    if not visited[r][c]:
        visited[r][c] = 1
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N:
            # 조건 좀 똑바로 읽자, 높이가 같아도 못 간다.
            if g[nr][nc] < g[r][c] and not visited[nr][nc]:
                do(nr, nc, flag)
                visited[nr][nc] = 0
            # 만약 다 도는 중 아직 안 갂아냈는데 다음 지역이 더 높거나 같은 높이라면
            elif g[nr][nc] >= g[r][c] and not visited[nr][nc] and flag == 1:
                # 그 지역을 1부터 k만큼 깎아내면서 확인한다.
                for k in range(1, K+1):
                    g[nr][nc] -= k
                    # 만약 깎은 후 다시 높이가 커졌다면, 들어가되 플래그를 막은 채로 넣는다.
                    if g[nr][nc] < g[r][c]:
                        do(nr, nc, 0)
                        visited[nr][nc] = 0
                        flag = 1
                    g[nr][nc] += k
    else:
        # 사실 이 값을 가져가는 방법이 있을 텐데, 생각하기 귀찮아서 그냥 세었다.
        # 다시 풀 때는 한 번 가져가보자.
        cnt = 0
        for x in range(N):
            for y in range(N):
                if visited[x][y] == 1:
                    cnt += 1
        if cnt > max_v:
            max_v = cnt


for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 방향델타: 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 그래프 초기화
    g = []
    max_height = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        temp_v = max(temp)
        if temp_v > max_height:
            max_height = temp_v
        g.append(temp)

    # 방문여부와 최대값 초기화
    visited = [[0] * N for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            # 가장 높은 놈들 좌표를 배열에 넣기
            if g[i][j] == max_height:
                do(i, j, 1)
                # 이거 꼭 해줘야 한다. => 처음 들어가는 좌표는 백트래킹이 불가하기 때문
                visited[i][j] = 0
    print(f'#{tc} {max_v}')


