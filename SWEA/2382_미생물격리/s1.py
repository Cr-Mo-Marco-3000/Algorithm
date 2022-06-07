import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 없, 상, 하, 좌, 우
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def reverse(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3

def do1():
    for k in range(len(germ_list)):
        germ = germ_list[k]
        r = germ[0]
        c = germ[1]
        nr = r + dr[germ[3]]
        nc = c + dc[germ[3]]
        germ[0] = nr
        germ[1] = nc

def do2():
    for l in range(len(germ_list)):
        germ = germ_list[l]
        r = germ[0]
        c = germ[1]
        if r == 0 or r == N-1 or c == 0 or c == N-1:
            germ[2] = germ[2] // 2
            germ[3] = reverse(germ[3])

def do3():
    g = [[[] for _ in range(N)] for _ in range(N)]
    for m in range(len(germ_list)):
        germ = germ_list[m]
        g[germ[0]][germ[1]].append(m)
    for i in range(N):
        for j in range(N):
            if len(g[i][j]) > 1:
                do4(g[i][j])


def do4(cells):
    total_number = 0
    # max_number와 max_cell을 0으로 했을 때는 오답이 나왔는데 왜 그럴까?
    # max_number가 문제라는데
    # 인덱스, 수 오차가 나지 않게 하기 위해 초기값을 그냥 첫 번째로 설정해줬다.
    max_cell = cells[0]
    max_number = germ_list[cells[0]][2]
    for cell in cells:
        total_number += germ_list[cell][2]
        if germ_list[cell][2] > max_number:
            max_cell = cell
            max_number = germ_list[cell][2]
    for cell in cells:
        germ_list[cell][2] = 0
    germ_list[max_cell][2] = total_number



for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 한 변에 있는 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    # 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
    # c, r, num, d

    germ_list = []
    for i in range(K):
        germ_list.append(list(map(int, input().split())))
    for _ in range(M):
        # 미생물 이동
        do1()
        # 경계 미생물 반전
        do2()
        # 군집 합쳐짐 확인 후 변경
        do3()
    total = 0
    for cnt in range(len(germ_list)):
        total += germ_list[cnt][2]
    print('#{} {}'.format(tc, total))

