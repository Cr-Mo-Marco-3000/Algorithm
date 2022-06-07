import sys

sys.stdin = open('input.txt')

def do(v):
    if g[v][3] != 0:
        do(g[v][0])
        print(g[v][3], end='')
    # if g[v][1] != 0:
        do(g[v][1])

T = 10


for tc in range(1, T+1):
    N = int(input())

    g = [[0] * 4 for _ in range(N+1)]
    for i in range(1, N+1):
        string = list(map(str, input().split()))
        if len(string) == 4:
            nod, character, l, r = string
            nod = int(nod)
            l = int(l)
            r = int(r)

            g[nod][0] = l
            g[nod][1] = r
            g[nod][3] = character
            g[l][2] = i
            g[r][2] = i

        elif len(string) == 3:
            nod, character, l = string
            nod = int(nod)
            l = int(l)

            g[nod][0] = l
            g[nod][3] = character
            g[l][2] = i

        else:
            nod, character = string
            nod = int(nod)
            g[nod][3] = character

        nod, l, r, character = 0, 0, 0, 0
        # left right parent alpha
    print('#{} '.format(tc, ), end='')
    do(1)
    print()



