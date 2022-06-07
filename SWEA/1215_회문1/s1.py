import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 찾아야 하는 회문의 길이 M
    # my_list의 가로 세로 길이 N
    M = int(input())
    N = 8
    cnt = 0
    my_list = [list(map(str, input())) for _ in range(N)]
    for i in range(N): # 실수한 부분
        for j in range(N - M + 1):
            if my_list[i][j:j+M] == my_list[i][j:j+M][::-1]:
                cnt+=1
    my_list = list(zip(*my_list))
    for i in range(N):
        for j in range(N - M + 1):
            if my_list[i][j:j+M] == my_list[i][j:j+M][::-1]:
                cnt+=1
    print('#{} {}'.format(tc, cnt))

