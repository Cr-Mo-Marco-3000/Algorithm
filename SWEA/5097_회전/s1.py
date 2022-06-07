import sys
from collections import deque

sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Q = deque(map(int, input().split()))
    for _ in range(M):
        Q.rotate(-1)
    print(f"#{tc} {Q[0]}")
