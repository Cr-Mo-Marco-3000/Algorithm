import sys
from collections import deque
sys.stdin = open('sample_input.txt')

# 이따위 문제 틀리지 말자
# counts에 1씩 더해주는 것이 아니라, 특정 숫자로 갱신해주는 문제다.

def carving(carving_list, N, Q):
    counts = deque([0] * (N + 1))
    for i in range(0, len(carving_list)):
        for j in range(carving_list[i][0], carving_list[i][1] + 1):
            counts[j] = i + 1
    counts.popleft()
    print(f'#{tc} ', end="")


T = int(input())


for tc in range(1, T+1):
    N, Q = map(int, input().split())
    carving_list = []
    for _ in range(Q):
        carving_list.append(list(map(int, input().split())))
    carving(carving_list, N, Q)

