N, M = map(int, input().strip().split())


my_list = [0] * N
def do(i):
    if i == N:
        if sum(my_list) == M:
            print(*my_list)
            return
        else:
            return
    else:
        for w in range(1, 7):
            my_list[i] = w
            do(i+1)

do(0)
