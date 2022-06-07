import sys

sys.stdin = open('input.txt')

def sdoku(my_list, reversed_list, squared_list):
    for i in range(9):
        # 일반행렬, 전치행렬, 3X3 격자행렬을 모두 정렬한 뒤, 정렬된 세 행렬 중을 순환하는 중 이전 값과 값이 같다면, False를
        # 순환을 완료하면 True를 반환한다.
        my_list[i].sort()
        reversed_list[i].sort()
        squared_list[i].sort()
        for j in range(8):
            if my_list[i][j] == my_list[i][j+1] or reversed_list[i][j] == reversed_list[i][j+1] or squared_list[i][j] == squared_list[i][j+1]:
                return 0
    else:
        return 1



T = int(input())

for tc in range(1, T+1):
    # N: 스토쿠의 길이
    N = 9
    my_list = [list(map(int, input().split())) for _ in range(N)]
    reversed_list = list(map(list, zip(*my_list)))
    squared_list = []
    middle_index = [1, 4, 7]
    delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,0], [0, 1], [1, -1], [1,0], [1, 1]]
    for i in middle_index:
        for j in middle_index:
            temp = []
            for k in range(N):
                # 각 3X3격자의 중앙점을 중심으로, 9방의 값을 더해 리스트를 만든다.
                temp.append(my_list[i + delta[k][0]][j + delta[k][1]])
            squared_list.append(temp)

    ans = sdoku(my_list, reversed_list, squared_list)

    print('#{} {}'.format(tc, ans))

