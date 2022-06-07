from sys import stdin
n, m = map(int, input().split())

s = []

def find(x):
    while s[x] != x:
        x = s[x]
    return x

for i in range(n+1):
    s += [i]

for i in range(m):
    cal, a, b = map(int, stdin.readline().rstrip().split())
    if cal:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    elif not cal:
        s[find(b)] = find(a)
