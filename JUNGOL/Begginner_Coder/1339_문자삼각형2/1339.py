N = int(input())

g = [[" "] * N for _ in range(N)]

if 1 <= N <= 100 and N % 2:
    cnt = 0

    j = N // 2

    si = N // 2
    ei = si + 1

    while j >= 0:
        for i in range(si, ei):
            g[i][j] = chr(65 + (cnt % 26))
            cnt += 1
        si -= 1
        ei += 1
        j -= 1

    for k in range(N):
        print(*g[k])
else:
    print("INPUT ERROR")