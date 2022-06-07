import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    tc = int(input())
    my_list = [list(map(str, input())) for _ in range(100)]
    max_length = 1
    # 좌 우 길이 100
    # 길이가 M인 회문을 구할 때
    for M in range(1, 101):
        for i in range(100):
            for j in range(100 - M + 1):
                if my_list[i][j:j+M] == my_list[i][j:j+M][::-1]:
                    if M >= max_length:
                        max_length = M

    my_list = list(zip(*my_list))
    for M in range(1, 101):
        for i in range(100):
            for j in range(100 - M + 1):
                if my_list[i][j:j+M] == my_list[i][j:j+M][::-1]:
                    if M >= max_length:
                        max_length = M

    print(f'#{tc} {max_length}')