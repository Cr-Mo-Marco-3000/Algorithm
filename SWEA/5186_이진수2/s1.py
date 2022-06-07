import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    n = float(input())
    i = 1
    string = ''
    while i <= 12:
        string += str(int(n // 2 ** -i))
        n = n % 2 ** -i
        if n == 0:
            break
        i += 1
    else:
        print('#{} {}'.format(tc, 'overflow'))
        continue
    print('#{} {}'.format(tc, string))

