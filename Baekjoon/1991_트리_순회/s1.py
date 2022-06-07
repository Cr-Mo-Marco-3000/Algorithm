from sys import stdin

V = int(stdin.readline().rstrip())

def do(v):
    if v:
        print(alpha_dict[v], end='')
        do(g[v][0])
        do(g[v][2])

def do2(v):
    if v:
        do2(g[v][0])
        print(alpha_dict[v], end='')
        do2(g[v][2])

def do3(v):
    if v:
        do3(g[v][0])
        do3(g[v][2])
        print(alpha_dict[v], end='')

g = [[0, 0, 0] for _ in range(V+1)]
# A == 65, Z == 90
alpha_dict = {}
for i in range(1, 27):
    alpha_dict[i] = chr(i + 64)
    alpha_dict[chr(i+64)] = i
    alpha_dict['.'] = 0



for _ in range(V):
    p, lc, rc = map(str, input().split())
    p = alpha_dict[p]
    lc = alpha_dict[lc]
    rc = alpha_dict[rc]
    g[p][0], g[p][2] = lc, rc


do(1)
print()
do2(1)
print()
do3(1)
