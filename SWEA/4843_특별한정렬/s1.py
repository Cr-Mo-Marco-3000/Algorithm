import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 덱써서 풀기
    N = int(input())
    my_list = list(map(int, input().split()))
    my_list.sort()
    my_deque = deque(my_list)
    new_list = []
    for i in range(10):
        if not i % 2:
            new_list.append(my_deque.pop())
        elif i % 2:
            new_list.append(my_deque.popleft())

    print('#{}'.format(tc), end=" ")
    print(*new_list)

