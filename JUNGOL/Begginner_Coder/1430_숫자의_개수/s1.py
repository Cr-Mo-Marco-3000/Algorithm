import sys

input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

num = A * B * C

C = [0] * 10

while num:
    c_num = num % 10
    C[c_num] += 1
    num //= 10

for i in C:
    print(i)

# // % 등으로 갖고 놀아야 한다. 처음에는 dict 쓰려다가 카운트 배열로 바꾸었다.

