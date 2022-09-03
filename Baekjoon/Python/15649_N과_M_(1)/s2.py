def do():
    if visited.count(1) == M:
        print(*ans_list)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans_list.append(my_list[i])
            do()
            visited[i] = 0
            ans_list.pop()




N, M = map(int, input().split())
my_list = []
check_list = [0] * N
for i in range(1, N+1):
    my_list.append(i)
visited = [0] * N
ans_list = []
do()