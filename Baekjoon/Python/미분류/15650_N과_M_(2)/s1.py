def punc(i):
    if i == N:
        if visited.count(1) == M:
            print(*ans_list)
            return
    # elif visited.count(1) >= M:
    elif visited.count(1) > M:
        return
    else:
        visited[i] = 1
        ans_list.append(my_list[i])
        punc(i+1)
        visited[i] = 0
        ans_list.pop()
        punc(i+1)



# N, M = map(int, input().split())
N, M = 4, 2
my_list = []

for i in range(1, N+1):
    my_list.append(i)
# visited를 활용하는 편이 편하겠다.
visited = [0] * N
ans_list = []
punc(0)