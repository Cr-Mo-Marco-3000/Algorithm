import sys

N = int(sys.stdin.readline().rstrip())

def do(N):
    if N <= 1:
        return 1
    else:
        return N * do(N-1)

print(do(N))