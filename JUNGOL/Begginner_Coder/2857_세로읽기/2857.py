import sys

input = sys.stdin.readline

g= []

for _ in range(5):
    temp = list(map(str, input().strip()))
    while len(temp) < 15:
        temp.append('')
    g.append(temp)

for j in range(15):
    for i in range(5):
        if g[i][j]:
            print(g[i][j], end="")

# 배고파서 조건이 잘 안 읽혔다
# 분명히 SWEA에서 예전에 풀었던 문제이다.