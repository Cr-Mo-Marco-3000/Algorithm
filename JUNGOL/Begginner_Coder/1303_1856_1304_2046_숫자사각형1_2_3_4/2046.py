N, M = map(int, input().strip().split())

if M == 1:
    for i in range(N):
        for j in range(N):
            print(i + 1, end=" ")
        print()

elif M == 2:
    for i in range(N):
        for j in range(N):
            if not i % 2:
                print(j + 1, end=" ")
            else:
                print(N - j, end=" ")
        print()

else:
    for i in range(N):
        for j in range(N):
            print((j+1)*(i+1), end=" ")
        print()