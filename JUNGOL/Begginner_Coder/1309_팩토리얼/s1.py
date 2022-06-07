import sys

input = sys.stdin.readline

def do(i):
    if i == 1:
        print('1! = 1')
        return 1
    else:
        print(f'{i}! = {i} * {i-1}!')
        return i * do(i-1)

N = int(input())

print(do(N))

# 팩토리얼은 많이 풀어 본 문제이긴 한데, 출력 조건이 까다로웠다
# 핵심적인 부분은, 탈출하는 base case와, base_case가 아닐 경우 return에 특정 값과 재귀 함수를 호출하는 것!
# 리턴 값에 수식이나 값을 넣는 것을 주저하지 말자!