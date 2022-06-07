import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 2번에서 쓸 것
num_list = [1] * N

my_set = []



def do1(i):
    if i == N:
        print(*num_list)
    else:
        while num_list[i] < 7:
            do1(i + 1)
            num_list[i] += 1
        num_list[i] = 1

def do2(i):
    if i == N:
        C = [0] * 7
        for i in range(N):
            C[num_list[i]] += 1
        if C in my_set:
            return
        else:
            print(*num_list)
            my_set.append(C)
    else:
        while num_list[i] < 7:
            do2(i + 1)
            num_list[i] += 1
        num_list[i] = 1

# 3번에서 쓸 것

N_list = [0] * (N)
visited = [0] * 7

def do3(i):
    if i == N:
        print(*N_list)
    else:
        for w in range(1, 7):
            if not visited[w]:
                visited[w] = 1
                N_list[i] = w
                do3(i+1)
                visited[w] = 0
                N_list[i] = 0

if M == 1:
    do1(0)
elif M == 2:
    do2(0)
elif M == 3:
    do3(0)

# 1번 케이스는 단순 나열 문제
# 2번 케이스는 set을 활용해서 중복을 제거했는데, 다른 방법도 있을 것 같다.
# 3번 케이스는 조합 문제가 아니었다...