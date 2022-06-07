import sys
from collections import deque
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_dict = {}
    for i in range(1, M+1):
        pizza_dict[i] = pizza[i-1]

    oven = deque(range(1, N + 1))
    outside = deque(range(N+1, M+1))

    while len(oven) != 1:
        v = oven.popleft()
        cheeze = pizza_dict[v] // 2
        if cheeze == 0 and outside:                 # 치즈가 0이고 밖에 피자가 남아 있을 때,
            oven.appendleft(outside.popleft())      # 피자를 오븐에서 뺀다.
        elif cheeze == 0 and not outside:           # 치즈가 0이고 밖에
            continue
        else:
            oven.appendleft(v)
            pizza_dict[v] = cheeze
        oven.rotate(-1)

    print('#%d %d' % (tc, oven[0]))