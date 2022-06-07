import sys
import operator
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    N = int(input())
    stack = []
    my_list = []
    my_string = input()
    # 우선순위가 생각보다는 쓰일 때가 적지만, 그래도 dict에 저장해 줬다.
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2} # in-coming-priority
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2} # in-stack-priority
    for i in my_string:
        if i == '(': # 여는 괄호는 바깥에서는 무적이므로, 무조건 push
            stack.append(i)
        elif i == ')':                                  # 닫는 괄호가 나오면, 여는 괄호가 나올 때 까지 팝, 프린트
            while stack[-1] != '(':                     # 닫는 괄호는 교육 지원금처럼 스칠뿐, 여는 괄호와 함께, 사라진다.
                my_list.append(stack.pop())
            stack.pop()
        elif i in '+-':
            while stack and isp[stack[-1]] >= icp[i]:   # +,-가 나오면, 스택에 항목이 존재하고,
                my_list.append(stack.pop())              # 맨 위 항목 우선순위가 같거나 높다면 더 낮은 애가 나올때까지 pop
            stack.append(i)                             # 빼내서 출력이 끝나면 추가
        elif i in '*/':
            while stack and isp[stack[-1]] >= icp[i]:   # *,/가 나오면, 스택에 항목이 존재하고,
                my_list.append(stack.pop())              # 맨 위 항목 우선순위가 같거나 높다면 더 낮은 애가 나올때까지 pop
            stack.append(i)                             # 빼내서 출력이 끝나면 추가
        else:
            my_list.append(i)
    while stack:
        my_list.append(stack.pop())

    # 아래는 연산

    stack = []
    for i in my_list:
        if i == "/":
            b = stack.pop()
            a = stack.pop()
            c = a / b
            stack.append(c)
        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            c = a * b
            stack.append(c)
        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            c = a + b
            stack.append(c)
        elif i == '-':
            b = stack.pop()
            a = stack.pop()
            c = a - b
            stack.append(c)
        else:
            stack.append(int(i))
    else:
        print(f'#{tc} ', end='')
        print(stack[0])

