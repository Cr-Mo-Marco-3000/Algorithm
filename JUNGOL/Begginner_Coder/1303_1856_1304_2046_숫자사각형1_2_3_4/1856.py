N, M = map(int, input().strip().split())

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i % 2): # 홀수줄일 경우
            print((i-1) * M + j, end=" ")
        else: # 짝수줄일 경우
            print(f'{i * M - j + 1}', end=" ")
    print()