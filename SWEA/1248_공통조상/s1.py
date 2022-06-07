import sys

sys.stdin = open('input.txt')

T = int(input())


def do(s):
    if s:
        list_1.append(g[s][1])
        do(g[s][1])


def do2(s):
    if s:
        list_2.append(g[s][1])
        do2(g[s][1])


def do3(s):
    global cnt
    cnt += 1
    if g[s][0]:
        do3(g[s][0])
    if g[s][2]:
        do3(g[s][2])


for tc in range(1, T+1):
    # 트리의 정점의 총 수 V와 간선의 총 수 E, 공통 조상을 찾는 두 개의 정점 번호 a, b
    V, E, a, b = map(int, input().split())
    temp = list(map(int, input().split()))
    g = [[0, 0, 0] for _ in range(V+1)]
    for i in range(E):
        if not g[temp[2*i]][0]:
            g[temp[2*i]][0] = temp[2*i + 1]
        else:
            g[temp[2 * i]][2] = temp[2*i + 1]
        g[temp[2*i + 1]][1] = temp[2*i]
    # print(g)
    list_1 = []
    list_2 = []
    do(a)
    do2(b)
    for i in list_1:
        for j in list_2:
            if i == j:
                ans_1 = i
                break
        if i == j:
            break
    cnt = 0
    do3(ans_1)
    ans_2 = cnt

    print('#{} {} {}'.format(tc, ans_1, ans_2))

