import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split()) # N: 퍼즐의 길이, K: 단어의 길이
    cnt = 0 # 들어가는 단어의 개수
    my_list = [list(map(int, input().split())) for _ in range(N)]
    reversed_list = list(map(list, zip(*my_list)))
    # for i in range(my_list): i = [0] + i + [0]는 왜 안될까? => my_list의 i을 참조하는 것이 아니라, 거기서 값을 빼오는 것!
    # 처음에 그냥 행렬, 전치 행렬 두 개를 만들어 주고, 인덱스 에러를 방지하기 위해 좌 우에 [0]을 붙인다.
    for _ in range(len(my_list)):
        my_list[_] = [0] + my_list[_] + [0]
    for _ in range(len(reversed_list)):
        reversed_list[_] = [0] + reversed_list[_] + [0]
    # 카운팅할 변수 초기화
    cnt = 0
    for i in range(N):
        for j in range(0, N + 2 - K):
            if my_list[i][j] == 1:
                for k in range(0, K):
                    if my_list[i][j+k] != 1:
                        break
                else:
                    if my_list[i][j+k+1] == 0 and my_list[i][j-1] == 0:
                        cnt += 1
    for i in range(N):
        for j in range(0, N + 2 - K):
            if reversed_list[i][j] == 1:
                for k in range(0, K):
                    if reversed_list[i][j + k] != 1:
                        break
                else:
                    if reversed_list[i][j + k + 1] == 0 and reversed_list[i][j - 1] == 0:
                        cnt += 1
    print('#{} {}'.format(tc, cnt))
