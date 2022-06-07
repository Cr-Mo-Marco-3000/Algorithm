import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    length, string = map(str, input().split())
    num = 0
    N = int(length)
    for i in range(N-1, -1, -1):
        if '0' <= string[i] <= '9':
            a = ord(string[i]) - ord('0')
        elif 'A' <= string[i] <= 'F':
            a = ord(string[i]) - ord('A') + 10
        num += 16 ** (N - 1 - i) * a
    number = str(bin(num)[2:])
    while len(number) % 4:
        number = '0' + number
    print(f'#{tc} {number}')

