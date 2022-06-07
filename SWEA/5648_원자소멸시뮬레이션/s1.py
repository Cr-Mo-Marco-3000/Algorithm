T = int(input())
# 상 하 좌 우
dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)

for tc in range(1, T+1):
    N = int(input())
    # 원소 리스트 my_list
    my_list = []
    total = 0
    for _ in range(N):
        #  N개의 줄에는 원자들의 x 위치, y 위치, 이동 방향, 보유 에너지 K
        x, y, d, k = map(int, input().split())
        x += 1000
        y += 1000
        total += k
        my_list.append([x, y, d, k])
    # total = 0
    for _ in range(2001): # 2000번 돌리면 되지 않을까?
        if not my_list:
            break
        # 1. 원소 이동
        for i in my_list:
            i[1] += dr[i[2]]
            i[0] += dc[i[2]]

        # 세로 교차 파괴: x축, y축 순으로 정렬

        my_list.sort(key=lambda ball: (ball[0], ball[1]))
        i = 0
        while i < len(my_list) - 1:
            if my_list[i][0] == my_list[i+1][0]: # x축의 좌표가 같은데
                if abs(my_list[i][1] - my_list[i+1][1]) == 1: # y축의 좌표 차이 절대값이 1이고
                    if my_list[i][2] == 1 and my_list[i+1][2] == 0: # 위에 있는 게 방향이 위쪽, 아래 있는 게 방향이 아래쪽(즉 교차했으면)
                        my_list[i][0] = -2
                        my_list[i+1][0] = -2
                        my_list[i][1] = -2
                        my_list[i + 1][1] = -2
                        continue
            i += 1

        # 가로 교차 파괴: y축, x축 순으로 정렬
        my_list.sort(key=lambda ball: (ball[1], ball[0]))
        i = 0
        while i < len(my_list) - 1:
            if my_list[i][1] == my_list[i + 1][1]:  # y축의 좌표가 같은데
                if abs(my_list[i][0] - my_list[i + 1][0]) == 1:  # x축의 좌표 차이 절대값이 1이고
                    if my_list[i][2] == 2 and my_list[i+1][2] == 3:  # 오른쪽에 있는 게 방향이 오른쪽, 왼쪽 => 왼쪽
                        my_list[i][0] = -2
                        my_list[i + 1][0] = -2
                        my_list[i][1] = -2
                        my_list[i + 1][1] = -2
                        continue
            i += 1
        my_list.sort(key=lambda ball: (ball[1], ball[0]), reverse=True)

        while my_list and my_list[len(my_list) - 1][0] == -2:
            my_list.pop()
        # 모이는 거 파괴
        j = 0
        while j < len(my_list):
            r = my_list[j][0]
            c = my_list[j][1]
            cnt = 0
            for k in range(1, 4):
                if 0 <= j + k < len(my_list):
                    if my_list[j + k][0] == r and my_list[j+k][1] == c:
                        cnt += 1
            if cnt > 0:
                for _ in range(cnt + 1):
                    my_list.pop(0)
                continue
            j += 1



    # 돌린 후 남은 에너지를 빼준다.
    for ans in my_list:
        total -= ans[3]

    print('#{} {}'.format(tc, total))

