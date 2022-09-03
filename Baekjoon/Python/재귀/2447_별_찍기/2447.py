import sys
input = sys.stdin.readline
N = int(input().strip())
M = 0
while N != 1:
    N = N //3
    M += 1
print(M)

def do(K):
    if K == 1:
        print()