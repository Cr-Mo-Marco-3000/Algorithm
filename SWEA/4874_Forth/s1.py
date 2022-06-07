import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    stack = []
    my_list = list(map(str, input().split()))
    try:
        for i in my_list:
            if i == '+':
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)
            elif i == '-':
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)
            elif i == '*':
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            elif i == '/':
                b = stack.pop()
                a = stack.pop()
                c = a // b
                stack.append(c)
            elif i == '.':
                if len(stack) == 1:
                    ans = stack.pop()
                    print(f'#{tc} {ans}')
                else:
                    print(f'#{tc} error')
                    break
            else:
                stack.append(int(i))
    except:
        print(f'#{tc} error')