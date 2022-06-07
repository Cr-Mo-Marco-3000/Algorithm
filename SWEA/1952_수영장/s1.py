import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do():
    global t_list
    if sum(t_list) == 12:
        case_list.append(t_list[:])
        return
    elif sum(t_list) > 12:
        return
    else:
        for d in [1, 3]:
            t_list.append(d)
            do()
            t_list.pop()

case_list = []
t_list = []
do()


for tc in range(1, T+1):
    aday, amonth, tmonth, ayear = map(int, input().split())
    my_list = list(map(int, input().split()))
    day_list = [0] * 12
    month_list = [0] * 12
    dm_list = []
    ans = ayear
    for i in range(12):
        # 한달 이용권과 하루 이용권 중 더 싼거 dm_list에 저장
        temp = min(amonth, aday * my_list[i])
        dm_list.append(temp)

    # 1과 3을 중복 사용해서 12를 만드는 경우의 수가 case_list
    for case in case_list:
        k = 0
        l = 0
        total = 0
        while l < 12:
            if case[k] == 1:
                total += dm_list[l]
                k += 1
                l += 1
            elif case[k] == 3:
                if sum(my_list[l:l+3]):
                    total += tmonth
                    k += 1
                    l += 3
                else:
                    k += 1
                    l += 3
        if total < ans:
            ans = total

    print('#{} {}'.format(tc, ans))

