import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    nums = list(map(int, input().split()))
    alpha = max(nums)
    omega = min(nums)

    print('#{} {}'.format(tc, alpha - omega))

