def do(j):
    visited[j] = 1
    ans_list.append(my_list[j])
    if visited.count(1) == M:
        print(*ans_list)
    else:
        for k in range(N):
            if not visited[k]:
                do(k)
                visited[k] = 0
                ans_list.pop()



N, M = map(int, input().split())
# N, M = 4, 4
my_list = []
check_list = [0] * N
for i in range(1, N+1):
    my_list.append(i)
visited = [0] * N
ans_list = []
for j in range(N):
    do(j)
    visited = [0] * N
    ans_list = []


