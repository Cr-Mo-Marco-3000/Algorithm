import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 의석이가 입력하는 줄 수 5 = N
    N = 5
    max_len = 0
    my_list = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        if len(my_list[i]) > max_len:
            max_len = len(my_list[i])

    # 길이가 최대인 행을 찾는다.
    # 그 길이에 맞춰서, 입력된 행에 의석이가 쓰지 않는 문자인 !을 더해준다.
    for j in range(N):
        while len(my_list[j]) < max_len:
            my_list[j].append("!")
    # 출력을 위해 전치행렬을 만든다.
    my_list = list(zip(*my_list))

    # 순환하며, 만약 문자가 !가 아니면 출력한다.
    print('#{} '.format(tc), end="")
    for i in range(max_len):
        for j in range(5):
            if my_list[i][j] != '!':
                print(my_list[i][j], end="")
    print()

