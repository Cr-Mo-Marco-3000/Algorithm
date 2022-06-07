import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 각각 한번 충전으로 이동 가능, 종점, 충전기 수
    movable, end, charger = map(int, input().split())
    # 충전기가 설치된 위치
    charger_list = list(map(int, input().split()))
    # 시작점과 종점을 리스트에 더해줌
    charger_list.append(end)
    charger_list.insert(0, 0)
    # 버스 위치
    bus_index = 0
    # 충전 횟수
    charge_count = 0
    # 만약 충전기들 사이에, 한 번에 움직일 수 있는 거리보다 긴 구간이 있다면 0을 출력하고 break
    for i in range(len(charger_list)-1):
        if charger_list[i+1] - charger_list[i] > movable:
            print('#{} {}'.format(tc, 0))
            break
    else:
        # 버스의 위치가 종점보다 뒤에 있을 경우
        while bus_index < end:
            # 충전한 만큼 갔을 때 정확히 충전기에 도달했을 때
            if (bus_index + movable) in charger_list:
                bus_index += movable
                charge_count += 1
            # 갔을 때 충전기가 없으면, 최대 주행거리에서 1씩 빼주다 충전소가 나오면 그 곳을 버스 위치로 삼고 +1을 해준다.
            else:
                for j in range(movable, 0, -1):
                    if bus_index + j in charger_list:
                        bus_index = bus_index + j
                        charge_count += 1
                        break
        # 처음 출발할 때도 충전횟수를 +1 해줬으므로 -1 해준다.
        charge_count -= 1
        print('#{} {}'.format(tc, charge_count))