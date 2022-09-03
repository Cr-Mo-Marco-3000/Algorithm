def crmo():
    if len(ans_list) == M:
        print(*ans_list)
        return
    elif len(ans_list) < M:
        for i in range(N):
            ans_list.append(my_list[i])
            crmo()
            ans_list.pop()




N, M = map(int, input().split())
# N, M = 3, 3
my_list = []

for i in range(1, N+1):
    my_list.append(i)

ans_list = []
crmo()
