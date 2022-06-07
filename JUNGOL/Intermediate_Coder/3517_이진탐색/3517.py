import sys


def do(q, l, r):
    if l > r:
        return -1
    else:
        mid =

input = sys.stdin.readline

N = int(input().strip())

array = list(map(int, input().strip().split()))

Q = int(input().strip())

Qs = tuple(map(int, input().strip().split()))


for item in Qs:
    do(item, 0, N-1)