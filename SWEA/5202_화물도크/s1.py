import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def do(cnt, ans):
    global total_ans
    if cnt == N:
        if ans > total_ans:
            total_ans = ans
        return
    elif ans + N - cnt < total_ans:
        return
    else:
        task = task_list[cnt]
        for i in range(task[0], task[1]):
            if visited[i]:
                do(cnt + 1, ans)
                return

        else:
            for i in range(task[0], task[1]):
                visited[i] = 1
            task_visited[cnt] = 1
            do(cnt + 1, ans + 1)
            for i in range(task[0], task[1]):
                visited[i] = 0
            task_visited[cnt] = 0
            do(cnt + 1, ans)


for tc in range(1, T+1):
    N = int(input())
    task_list = []
    for _ in range(N):
        task_list.append(tuple(map(int, input().split())))
    task_list.sort()
    task_visited = [0] * N
    visited = [0] * 24
    total_ans = 0
    do(0, 0)
    print('#{} {}'.format(tc, total_ans))

