import sys

N = int(sys.stdin.readline().strip())

def do(N):
    if N == 0:
        return 0
    if N <= 2:
        return 1
    else:
        return do(N-1) + do(N-2)

print(do(N))