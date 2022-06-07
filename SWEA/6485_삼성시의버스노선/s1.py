import sys

sys.stdin = open('s_input.txt')

def bus_stop(bus_list, stop_list, N, P):
    '''
    :param bus_list: 버스노선
    :param stop_list: 출력할 정류장들 리스트
    :param N: 버스노선 수
    :param P: 버스정류장 수
    :return:
    '''
    a = bus_list[0][1]
    counts = [0] * 5001 # 왠지 엄청 큰 값이 주어질 수도 있을 것 같아, 모든 버스정류장을 잡아줬다. 0~5000까지 있다.
    for i in bus_list: # 여기서는 조건이 무조건 i[0] < i[1] 이지만, 함정을 파 놓을 수도 있을 것이다. 이동 문제는 항상 주의하자.
        for j in range(i[0], i[1] + 1): # i 대신 bus_list[i] 썼다가 오류가 떴다.
            counts[j] += 1
    print(f'#{tc} ', end="")
    for k in stop_list:
        print(counts[k], end=" ")
    print()






T = int(input())


for tc in range(1, T+1):
    # N: 버스 노선의 수
    N = int(input())
    bus_list = []
    stop_list = []
    for i in range(N):
        bus_list.append(list(map(int, input().split())))
    # P: 정류장의 수
    P = int(input())
    for j in range(P):
        stop_list.append(int(input()))
    bus_stop(bus_list, stop_list, N, P)


