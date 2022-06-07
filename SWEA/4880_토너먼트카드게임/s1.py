import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def compare(a, b):               # 가위:1, 바위:2, 보:3 => 미리 적어놓고 풀 껄 그랬다.
    if my_dict[a] == my_dict[b]: # 가위바위보에서 같은 걸 내면
        return a                 # 앞에 있는 놈이 승리
    elif my_dict[a] == 1:        # a 가 가위를 내면
        if my_dict[b] == 2:      # b 가 바위를 내면 b 승
            return b
        elif my_dict[b] == 3:    # b 가 보자기를 내면 a 승
            return a
    elif my_dict[a] == 2:        # 이하는 같은 방식으로 비교한다.
        if my_dict[b] == 1:
            return a
        elif my_dict[b] == 3:
            return b
    elif my_dict[a] == 3:
        if my_dict[b] == 1:
            return b
        elif my_dict[b] == 2:
            return a


def rcp(input_list):
    i = 0
    j = len(input_list) - 1                             # start, end를 문제에서 제시한 대로 i, j로 지정해준다.
    if len(input_list) == 1:                            # 길이가 하나인 건 즉시 반환
        return input_list[0]
    elif len(input_list) == 2:                          # 길이가 두 개라면 가위바위보 함수에 넣는다.
        return compare(input_list[0], input_list[1])
    else:
        k = rcp(input_list[0:(i+j)//2 + 1])             # 만약 길이가 2 이상이라면
        d = rcp(input_list[((i+j)//2) + 1 : j+1])       # 두 개로 쪼개서 가위바위보 함수에 넣는다. 슬라이싱 영역 주의!
        return compare(k, d)






for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    input_list = [i for i in range(1, N+1)] # 1부터 N까지 학생들 번호의 리스트를 만든다.
    my_dict = {}
    for i in range(len(my_list)):
        my_dict[i+1] = my_list[i] # 학생들 번호에 가위바위보를 배정한다.
    ans = rcp(input_list)
    print('#{} {}'.format(tc, ans))

