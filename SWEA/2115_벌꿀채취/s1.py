import sys
from itertools import permutations
sys.stdin = open('sample_input.txt')

T = int(input())

def do(arr):                                # 어떤 경우의 수에서 벌 수 있는 돈을 찾는다.
    money = 0
    per_list = tuple(permutations(arr, M))
    for per in per_list:
        cnt = 0
        temp_money = 0
        for j in per:
            cnt += j
            if cnt > C:
                break
            temp_money += j ** 2
        if temp_money > money:
            money = temp_money
    return money

for tc in range(1, T+1):
    # 벌집 크기 N, 채취 벌통 크기 M, 채취량 C
    N, M, C = map(int, input().split())
    honey_list = []
    for i in range(N):
        temp = list(map(int, input().split()))
        # 벌통 한 줄을 순환
        for j in range(N - M + 1):
            # 채집 리스트에 넣음(최대 채취량,행, 처음 값, 끝 값)
            arr = temp[j: j+M]
            honey = [do(arr), i, j, j + M - 1]
            honey_list.append(honey)
    honey_list.sort(reverse=True)               # 채집 리스트는, 모든 채집 경우의 수 들이 매출의 순서대로 정렬되어 있는 값이다.

    # 궁합을 본다.
    ans = 0
    for i in range(0, len(honey_list)-1):       # 어떤 값과, 그 다음에 있는 값의 합이 겹치지 않으면서 최대가 되는 값을 찾는다.
        for j in range(i+1, len(honey_list)):
            a = honey_list[i]
            b = honey_list[j]
            if a[0] + b[0] < ans:
                break
            else:
                if a[1] != b[1]:
                    if a[0] + b[0] > ans:
                        ans = a[0] + b[0]
                        break                       # 만약 새로운 최대값을 갱신했다면, 이후의 값은 더 작은 값들이므로 더 볼 필요 없다.
                # 같은 행에 있으면
                if a[1] == b[1]:
                    if a[3] >= b[2] or a[2] <= b[3]:
                        continue                    # 만약 겹친다면, 이후 값을 탐색해야 한다.
                    else:
                        if a[0] + b[0] > ans:
                            ans = a[0] + b[0]
                            break                   # 만약 새로운 최대값을 갱신했다면, 이후의 값은 더 작은 값들이므로 더 볼 필요 없다.
    # 최대 채취량으로 정렬 후,
    # 겹치지 않은 하에서 고름
    print('#{} {}'.format(tc, ans))

