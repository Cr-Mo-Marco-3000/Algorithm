# 별삼각형 3
N = int(input())


if 1 <= N <= 100 and N % 2:
    my_list = []
    for i in range(1, N+1):
        if i < (N // 2) + 1:
            print(" " * (i - 1), end="")
            print("*" * (2*i - 1))
            my_list.append([i-1, 2*i - 1])
        elif i == (N//2) + 1 :
            print(" " * (i - 1), end="")
            print("*" * (2*i - 1))
        else: # i == 5 6 7 =>  7 중
            a, b = my_list.pop()
            print(" " * a, end="")
            print("*" * b)
else:
    print("INPUT ERROR!")

