import sys
input = sys.stdin.readline

def do(n, k):
    if k == 1:
        return n
    else:
        half = do(n, k // 2) % C
        if k % 2:
            return half * half * n
        else:
            return half * half

A, B, C = map(int, input().strip().split())
print(do(A, B) % C)