import sys

sys.stdin = open('input.txt')

def future(my_list, N):
    '''
    my_list: 날짜별 가격의 리스트
    N: 가격의 개수
    '''
    sell_list = [N-1]
    max_index = N-1                         # 오른쪽부터 접근하며, 이전 숫자보다 크면 거기서 팔아야지 손해를 보지 않는다.
    for i in range(N - 1, -1, -1):          # 예를 들어, 1 2 5 2 3 이라면, 3과 5에서 팔아야 한다.
        if my_list[i] > my_list[max_index]:
            sell_list.append(i)
            max_index = i
    sell_list.sort()

    # 판매하는 날들을 정렬시켜줬다.
    sell_len = len(sell_list)

    j = 0                       # 전체 인덱스
    k = 0                       # 판매하는 날의 인덱스, in이나 for 문을 통해 순환하며 비교하기보다 연산을 줄여주기 위해,1씩 증가시켜준다.
    cost = 0                    # 팔기 전 산 물품들의 비용
    buy = 0                     # 산 날들 횟수
    revenue = 0                 # 당기순이익
    while j < N:
        if j == sell_list[k]:                   # 만약 파는 날 리스트의 목록중 k-1 번째와 전체 인덱스 j가 일치한다면
            revenue += buy * my_list[j] - cost  # 현재 가격 * 구입한 횟수 - 총비용을 해서 당기순이익에 더해주고
            buy = 0                             # 재고를 털었으니 buy는 0
            cost = 0                            # 지금까지의 재고비용을 0 해준 후
            k += 1                              # 파는 날들 리스트의 인덱스를 다음으로 옮겨주고
            j += 1                              # 다음 날로 돌려준다.
        else:                                   # 살 때와 팔 때 케이스를 나누지 않고 해결하려다, 나누는 게 편하다는 걸 깨달았다. 주요 행동이 다르므로, 나누자.
            buy += 1                            # 하루에 하나만 살 수 있으므로 재고 + 1
            cost += my_list[j]                  # 구매 비용은 매일마다 달라지므로 += 해줘야 한다.
            j += 1                              # 하루 일과를 끝냈으면 다음 날로 옮겨준다.
    return revenue





T = int(input())

for tc in range(1, T+1):
    # N:
    N = int(input())
    my_list = list(map(int, input().split()))
    N = len(my_list)
    print('#{} {}'.format(tc, future(my_list, N)))

