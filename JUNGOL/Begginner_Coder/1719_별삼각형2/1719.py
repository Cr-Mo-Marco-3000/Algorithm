import sys

input = sys.stdin.readline

# 높이 n과 종류 m
n, m = map(int, input().rstrip().split())

if not n % 2:
    print("INPUT ERROR!")
else:
    if m == 1:
        cnt = 0
        for i in range(n):
            if i <= n // 2:
                cnt += 1
                print('*' * cnt)
            else:
                cnt -= 1
                print('*' * cnt)

    elif m == 2:
        cnt = 0
        for i in range(n):
            blank = n // 2 + 1
            if i <= n // 2:
                cnt += 1
                print(" " * (blank - cnt), end="")
                print('*' * cnt)
            else:
                cnt -= 1
                print(" " * (blank - cnt), end="")
                print('*' * cnt)

    elif m == 3:
        cnt = -1
        for i in range(n):
            if i <= n // 2:
                cnt += 1
                print(" " * cnt, end="")
                print("*" * (n - 2 * cnt), end="")
                print(" " * cnt, end="")
                print()
            else:
                cnt -= 1
                print(" " * cnt, end="")
                print("*" * (n - 2 * cnt), end="")
                print(" " * cnt, end="")
                print()

    elif m == 4:
        cnt = 0
        cnt2 = 2
        for i in range(n):
            if i <= n // 2:
                print(" " * cnt, end="")
                print("*" * (n // 2 - cnt), end="")
                print("*", end="")
                print()
                cnt += 1
            else:
                print(" " * (n // 2), end="")
                print("*" * cnt2, end="")
                print()
                cnt2 += 1
    else:
        print("INPUT ERROR!")

# 이렇게 코드를 조건별로 조각조각 내 놓는 것 보다 분명히 더 좋은 방법이 있겠지만
# 생각하기에는 시간이 너무 부족하고 아깝다.
# 다른 사람 코드를 볼 수 있으면 좋겠는데...