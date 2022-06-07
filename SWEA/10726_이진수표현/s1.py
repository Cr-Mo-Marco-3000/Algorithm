import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    bits, num = map(int, input().split())
    # num = bin(num)[2:]
    for i in range(bits):
        if num & (1 << i):
            continue
        else:
            print(f'#{tc} OFF')
            break
    else:
        print(f'#{tc} ON')

# if (((1 << N) - 1) & M) ^ ((1 <<N) - 1):
#     ans = 'off'
# else:
#     ans = 'on'