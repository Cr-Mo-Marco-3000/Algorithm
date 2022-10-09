import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())
my_list = list(map(int, input().strip().split()))
if N == 1:
    my_list.sort()
    print(sum(my_list) - my_list[-1])
else:
    min_one = min(my_list)
    my_dict = {}

    for i in range(6):
        my_dict[chr(65 + i)] = my_list[i]

    # 3면 중 최대
    three = ["ABC", "ACE", "ADE", "ABD", "BCF", "CEF", "DEF", "BDF"]
    min_three = sum(my_list)
    for i in three:
        total = 0
        for j in i:
            total += my_dict[j]
        if total < min_three:
            min_three = total

    # 2개의 면들 중 서로 붙어있는 면들만 남김
    two = []
    my_tuple = ("A", "B", "C", "D", "E", "F")
    temp = tuple(combinations(my_tuple, 2))
    for i in temp:
        if i in (('A', 'F'), ('B', 'E'), ('C', 'D')):
            continue
        else:
            two.append(i)

    # 두 개의 면들 중 최대값 구하기
    min_two = sum(my_list)
    for i in two:
        total = 0
        for j in i:
            total += my_dict[j]
        if total < min_two:
            min_two = total


    # 3개 면 노출 => 4개, 2개 면 노출(N-2 * 4 + N-1 * 4)개
    answer = min_three * 4 + min_two * ((N-2) * 4 + (N-1) * 4)
    answer += (N - 2) * (N - 2) * min_one * 5 + min_one * (N - 2) * 4

    print(answer)

    # 이게 도대체 무슨 문제지? 그냥 손으로 계산해서 풀었다...
    # 3면 경우의 수를 제대로 안 넣어주어 틀렸다... 이런 거 실수하지 맙시다.