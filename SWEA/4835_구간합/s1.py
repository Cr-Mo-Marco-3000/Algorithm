import sys

sys.stdin = open("sample_input.txt")

T = int(input())

# 정수의 갯수 N, 구간의 길이 M


for tc in range(T):
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    the_value = 0
    for i in range(M): # 초기값을 설정해준다.
        the_value += my_list[i]
    max_value = min_value = the_value

    j = 0
    while j < len(my_list) - M:
        the_value = the_value - my_list[j] + my_list[j+M]
        if the_value > max_value:
            max_value = the_value
        if the_value < min_value:
            min_value = the_value
        j += 1
        a = max_value - min_value
    print(f"#{tc} {a}")

