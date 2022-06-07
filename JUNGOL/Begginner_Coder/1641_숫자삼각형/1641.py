N, M = map(int, input().strip().split())

if 1 <= N <= 100 and N % 2 and 1 <= M <= 3:
    if M == 1:
        cnt = 1
        for i in range(N):
            temp = [i for i in range(cnt, cnt + 4)
            if not i % 2:

            else:

    elif M == 2:
        pass
    elif M == 3:
        pass
else:
    print("INPUT ERROR!")