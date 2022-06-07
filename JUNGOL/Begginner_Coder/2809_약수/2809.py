import math

N = int(input())
int(math.sqrt(N))
num_list = []

for i in range(1, int(math.sqrt(N)) + 1):
    if not N % i:
        print(i, end=" ")
        num_list.append(N // i)

if num_list[-1] == int(math.sqrt(N)):       # 마지막 약수가 자기 N의 제곱근일 경우에는
    num_list.pop()                          # 이미 프린트된 수가 num_list에 들어갈 수 있으므로, 뽑아주어야 한다.

while num_list:
    print(num_list.pop(), end=" ")