import sys
from pprint import pprint
sys.stdin = open('input.txt')

def do(start):
    Q = [start]
    while Q:
        r, c = Q.pop(0)
        # if g[r][c] == 3:                          # 도달할 수 있는지 여부만 판단하는 문제이므로 굳이 한번 더 들어갈 필요 없다.
        #     return 1                              # 바로 답을 도출해준다.
        g[r][c] = 1
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < 16 and 0 <= nc < 16:
                # if not g[nr][nc] or g[nr][nc] == 3:
                #     Q.append([nr, nc])
                if not g[nr][nc]:
                    Q.append([nr, nc])
                elif g[nr][nc] == 3:
                    return 1
    return 0


T = 10

for tc in range(1, T+1):
    tc = int(input())
    # ans = 0                                       # 거리를 체크하는 문제, 또는 재귀를 이용한다면 필요할 수도 있겠다.
    g = []
    dr = [-1, 0, 1, 0]                              # 언제 visited를 쓰고 언제 안 써야 할까?
    dc = [0, 1, 0, -1]
    for i in range(16):
        temp = list(map(int, input()))              # 한 줄씩 받아줘서 리스트로 만들어 준다
        for j in range(16):                         # 나중에 다시 한 번 순환하며 출발지와 도착지를 체크해주기 보다는
            if temp[j] == 2:                        # 처음에 받아줄 때 체크하는 게 약간이나마 연산을 줄일 수 있지 않을까?
                start = [i, j]
            elif temp[j] == 3:
                end = [i, j]
        g.append(temp)
    print('#{} {}'.format(tc, do(start)))

