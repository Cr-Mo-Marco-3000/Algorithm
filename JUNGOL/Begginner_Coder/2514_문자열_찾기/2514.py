import sys

input = sys.stdin.readline

string = input().strip()

N = len(string)

KOI = 0
IOI = 0

for i in range(N-2):
    if string[i:i+3] == 'KOI':
        KOI += 1
    elif string[i:i+3] == 'IOI':
        IOI += 1
print(KOI)
print(IOI)

# 안 풀어도 될 만큼 쉬운 문제