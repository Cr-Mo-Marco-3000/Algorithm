import sys

input = sys.stdin.readline

String = input().strip()
length = len(String)
N = int(String)

visited = [0] * length
ans = []
ans2 = 1000000000000
def do(cnt):
    global ans2
    if cnt == length:
        temp = int(''.join(ans))
        if N < temp and temp < ans2:
            ans2 = temp
    else:
        for i in range(length):
            if not visited[i]:
                visited[i] = 1
                ans.append(String[i])
                do(cnt+1)
                visited[i] = 0
                ans.pop()

do(0)
if ans2 == 1000000000000:
    print(0)
else:
    print(ans2)

