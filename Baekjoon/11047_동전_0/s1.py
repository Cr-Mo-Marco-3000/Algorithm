import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().rstrip().split())
coin_list = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num <= K:
        coin_list.append(num)
coin_list.reverse()
total = 0
for i in coin_list:
    total += K // i
    K = K % i
print(total)