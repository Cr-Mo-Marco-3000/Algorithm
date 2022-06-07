N, K = map(int, input().strip().split())

cnt = 0

for i in range(1, N+1):
    if not N % i:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(0)