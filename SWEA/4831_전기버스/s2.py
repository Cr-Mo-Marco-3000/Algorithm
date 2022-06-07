import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    movable, end, charger = map(int, input().split())     # 각각 한번 충전으로 이동 가능, 종점, 충전기 수
    charger_list = list(map(int, input().split()))        # 충전기가 설치된 위치 idx
    charger_list.append(end)                              # 시작점과 종점을 리스트에 더해줌
    charger_list.insert(0, 0)
    bus_index = 0                                         # 버스 위치
    charge_count = 0                                      # 충전 횟수

    count_list = [0] * (charger_list[-1] + movable + 1)   # 인덱스 에러를 만들지 않기 위해, count_list에  movable과 1을 더함
    for i in charger_list:
        count_list[i] += 1                                # 카운트 배열을 만듦

    for i in range(len(charger_list)-1):                  # 만약 충전기들 사이에,
        if charger_list[i+1] - charger_list[i] > movable: # 한 번에 움직일 수 있는 거리보다 긴 구간이 있다면
            print('#{} {}'.format(tc, 0))                 # 0을 출력하고 break
            break
    else:
        while bus_index < end:                            # 버스의 위치가 종점보다 뒤에 있을 경우에는 끝!
            for i in range(movable, -1, -1):              # 아닐 경우
                if count_list[bus_index + i] == 1:        # 최대 이동 거리부터 하나씩 빼 주며 버스의 현 위치에 더하다가
                    bus_index = bus_index + i             # 만약 그 위치에 충전기가 존재한다면 버스를 그 자리로 옮기고
                    charge_count += 1                     # 충전 수를 올리고
                    break                                 # 부뤠잌
                                                          # 부뤠잌 안하면 인덱스에 계속 더해줘서 망한다...
        charge_count -= 1                                 # 처음에도 주유를 한다고 계산했기에 1을 빼준다.
        print('#{} {}'.format(tc, charge_count))