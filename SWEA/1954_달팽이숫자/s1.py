import sys

sys.stdin = open('input.txt')

T = int(input()) # 2


for tc in range(1, T+1): # 2번 반복
    N = int(input())
    my_list = [[0] * N for _ in range(N)]
    # 상 우 하 좌
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    Limit = N * N # 반복횟수
    count = 1 # 초기 순서 숫자 설정
    r = 0  # 좌표 초기값 설정
    c = 0  # 좌표 초기값 설정
    d = directions[1] # 방향 초기값 = 우측 설정
    row_end = N - 1 # 각 열의 시작과 끝 좌표 설정
    row_start = 0
    column_end = N - 1
    column_start = 0
    criterion_num = 0 # 왼쪽 위에서만 돌리기 위한 설정이다.
    while count <= Limit:
        if row_start <= r <= row_end and column_start <= c <= column_end:
            my_list[r][c] = count # 현재 좌표가 범위 안에 있다면 숫자를 현재 자리에 대입한다.

        if r == row_start and c == column_end: # 만약 좌표가 맨 우측 상단이라면
            d = directions[2] # 방향을 하단으로 바꾼다.

        if r == row_end and c == column_end: # 만약 좌표가 맨 우측 하단이라면
            d = directions[3] # 방향을 좌측으로 바꾼다.

        if r == row_end and c == column_start: # 만약 좌표가 맨 좌측 하단이라면
            d = directions[0] # 방향을 위로 바꾼다.

        if r == row_start and c == column_start: # 만약 좌표가 처음을 제외한 좌측 상단이라면
            d = directions[1] # 방향을 우측으로 바꾼다.
        r += d[0]  # 현재 진행 방향으로 좌표를 하나씩 옮긴다.
        c += d[1]
        count += 1  # 대입할 숫자를 올린다.

        if r == c == criterion_num: # 만약 모서리로 복귀했다면
            r += 1 # 안쪽으로 하나씩 밀어넣고 기준도 1씩 줄인다.
            c += 1
            criterion_num += 1
            row_start += 1
            row_end -= 1
            column_start += 1
            column_end -= 1

    print('#{}'.format(tc))
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i][j], end=" ")
        print()


