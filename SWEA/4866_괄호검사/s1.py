import sys

sys.stdin = open('sample_input.txt')


def is_twin(my_string, N):
    my_list = []
    # 1 : (, 2 : {
    for i in range(N):
        if my_string[i] == '(':
            my_list.append(1)
        elif my_string[i] == '{':
            my_list.append(2)
        elif my_string[i] == ')':
            if not my_list or my_list[-1] != 1:
                return 0
            my_list.pop()
        elif my_string[i] == '}':
            if not my_list or my_list[-1] != 2:
                return 0
            my_list.pop()
    if my_list:
        return 0
    return 1


T = int(input())


for tc in range(1, T+1):
    my_string = input()
    N = len(my_string)
    ans = is_twin(my_string, N)
    print(f'#{tc} {ans}')