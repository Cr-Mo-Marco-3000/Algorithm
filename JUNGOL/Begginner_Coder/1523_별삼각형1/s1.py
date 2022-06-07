from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

if 1 <= n <= 100 and 1 <= m <= 3:
    if m == 1:
        for i in range(1, n + 1):
            print(f'{"*" * i}')
    elif m == 2:
        for i in range(n, 0, -1):
            print(f'{"*" * i}')
    elif m == 3:
        for i in range(1, n + 1):
            print(f'{" " * (n-i)}{"*" * (2*i-1)}')
else:
    print("INPUT ERROR!")

# 각 도형이 원하는 모양을 이루며 출력할 수 있도록 한다.
# 파이썬에서도 자바스크립트에서처럼 f스트링을 쓸 때 {} 안에 수식이 들어갈 수 있다.