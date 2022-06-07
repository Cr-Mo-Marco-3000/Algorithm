import sys
sys.stdin = open("input.txt")

for tc in range(1, 11): # 10번 반복
    x_length = int(input()) # 처음 가로 길이를 받는다.
    building_list = list(map(int, input().split())) # 빌딩 리스트를 받는다.
    idx = 2 # 건물이 3번째부터 있으므로, 2로 시작한다.
    total_view = 0
    while idx < x_length - 1:
        # 다른 답안에서 참고해 while문을 써보기로 했다. idx가 가로의 3번째부터 -3번째까지 순환한다.
        five_list = sorted(building_list[idx-2:idx+3])
        if five_list[-1] == building_list[idx]:
            total_view += (five_list[-1] - five_list[-2])
            # 가장 큰 높이에서, 두 번째로 높은 빌딩 높이를 빼줘 확보된 시야를 더해준다.
            # 만약 두 건물의 높이가 같아도, 더해지는 시야는 0이기에 정답에 영향을 미치지 않는다.
            idx += 2
            # 이 부분을 다른 분 코드에서 참고했는데,
            # 만약 한 건물이 조망권이 확보되었다면 다음 두 건물은 조망권이 확보되지 않았다는 뜻이니 넘어가 연산속도를 줄인다.
        idx += 1

    print('#{0} {1}'.format(tc, total_view))

