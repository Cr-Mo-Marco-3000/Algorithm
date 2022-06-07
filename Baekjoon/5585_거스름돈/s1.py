import sys

def hereisthechange(T):
    # N: 거스름돈
    # 거스름돈을 큰 잔돈 단위로 나누어 나가야 최소 개의 잔돈을 쓸 수 있다.
    N = 1000 - T
    a, i = N // 500, N % 500
    b, i = i // 100, i % 100
    c, i = i // 50, i % 50
    d, i = i // 10, i % 10
    e, i = i // 5, i % 5
    f = i // 1
    ans = a + b + c + d + e + f
    return ans

T = int(sys.stdin.readline().rstrip())
R = hereisthechange(T)
print(R)