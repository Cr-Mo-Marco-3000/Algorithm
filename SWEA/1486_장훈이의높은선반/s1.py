import sys

sys.stdin = open('input.txt')

T = int(input())

def do(i, N):
    global total
    global ans
    a = total - B
    if i == N:
        if 0 <= a < ans:
            ans = total - B
            return
    elif a > ans:
        return
    else:
        visited[i] = 1
        total += my_list[i]
        do(i+1, N)

        visited[i] = 0
        total -= my_list[i]
        do(i+1, N)



for _ in range(1, T+1):
    N, B = map(int, input().split())
    my_list = list(map(int, input().split()))
    # 백트래킹 써도 시간 초과 뜰 것 같은데...
    total = 0
    ans = B
    visited = [0] * N
    do(0, N)
    print('#{} {}'.format(_, ans))
