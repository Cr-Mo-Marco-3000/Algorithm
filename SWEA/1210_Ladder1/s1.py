import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    tc = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # direction delta: 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    
    # 마지막 행에서 2를 찾는다.
    for i in range(102):
        if ladder[99][i] == 2:
            start_column = i
    # 시작 위치는 ladder[99][i] 좌표 = 99, i, 처음 방향은 상
    ci, cj, cd = 99, start_column, 0

    # 만약 현재 방향 앞이 1이라면 전진
    while ci != 0:
        # 처음 전진
        # 처음, 좌우판단
        # 전진 중이고 좌,우측에 길이 있으면
        if cd == 0 and ladder[ci][cj + 1] == 1:
            cd = 1
            ci = ci + di[cd]
            cj = cj + dj[cd]
        elif cd == 0 and ladder[ci][cj - 1] == 1:
            cd = 3
            ci = ci + di[cd]
            cj = cj + dj[cd]
        # 현재 방향의 앞에 1이 있다면 전진
        if ladder[ci + di[cd]][cj + dj[cd]] == 1:
            ci = ci + di[cd]
            cj = cj + dj[cd]
        # 좌, 우측으로 가다 앞에 길이 없으면
        if cd == 1 or cd ==3:
            if ladder[ci + di[cd]][cj + dj[cd]] == 0:
                cd = 0
                ci = ci + di[cd]
                cj = cj + dj[cd]
    print(f'#{tc} {cj-1}')
