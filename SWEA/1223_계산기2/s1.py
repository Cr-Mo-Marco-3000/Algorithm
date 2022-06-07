import sys

sys.stdin = open('input.txt')

def make(my_string):
    stack = []
    operate_list = []
    for i in my_string:
        if i in '+-':
            if stack:
                while stack:
                    operate_list.append(stack.pop())
            stack.append(i)
        elif i in '*/':
            while stack and stack[-1] in '*/':
                operate_list.append(stack.pop())
            stack.append(i)
        else:
            operate_list.append(i)
    while stack:
        operate_list.append(stack.pop())
    return operate_list



def operating(after_make):
    stack = []
    for i in after_make:
        if i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif i == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif i == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            stack.append(int(i))
    return stack[0]


T = 10

for tc in range(1, T+1):
    N = int(input())
    my_string = input()
    # my_string = '3+4+5*6+7'
    after_make = make(my_string)
    ans = operating(after_make)
    print('#{} {}'.format(tc, ans))

