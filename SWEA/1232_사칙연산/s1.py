import sys
from pprint import pprint

sys.stdin = open('input.txt')

def do(S):
    if g[S][2] == '+':
        ans = do(g[S][0]) + do(g[S][1])
        return ans
    elif g[S][2] == '-':
        ans = do(g[S][0]) - do(g[S][1])
        return ans
    elif g[S][2] == '*':
        ans = do(g[S][0]) * do(g[S][1])
        return ans
    elif g[S][2] == '/':
        ans = do(g[S][0]) // do(g[S][1])
        return ans
    else:
        ans = g[S][2]
        return ans


for tc in range(1, 11):
    N = int(input())
    g = [[0, 0, 0, 0] for _ in range(N+1)]
    # 좌 우 내용물 부모
    # 0 0 숫자 부모
    for i in range(1, N + 1):
        temp = list(input().split())
        if len(temp) == 4:
            # nod번호 연산자 좌자 우자
            nod = int(temp[0])
            operator = temp[1]
            left = int(temp[2])
            right = int(temp[3])

            g[nod][0] = left
            g[nod][1] = right
            g[nod][2] = operator
            g[right][3] = nod
            g[left][3] = nod
        elif len(temp) == 2:
            nod, number = int(temp[0]), int(temp[1])
            g[nod][2] = number
    answer = do(1)
    print('#{} {}'.format(tc, answer))

