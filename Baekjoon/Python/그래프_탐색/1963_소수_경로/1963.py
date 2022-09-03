import sys, heapq
input = sys.stdin.readline

N = int(input().strip())

array = [10001] * 10001

def do(num):
    global ans
    my_list = array[:]
    heap = [(0, num)]
    while heap:
        cnt, num = heapq.heappop(heap)
        if num == end:
            ans = cnt
            return
        if my_list[num] > cnt:
            my_list[num] = cnt

            for i in range(1, 10):
                alt = num - (num % 10) + i
                if my_list[alt] > cnt + 1:
                    heap.append((cnt + 1, alt))
            for i in range(0, 10):
                alt = num - (num % 100) + (num % 10) + 10 * i
                if my_list[alt] > cnt + 1:
                    heap.append((cnt + 1, alt))
            for i in range(0, 10):
                alt = num - (num % 1000) + (num % 100)+ 100 * i
                if my_list[alt] > cnt + 1:
                    heap.append((cnt + 1, alt))
            for i in range(1, 10):
                alt = (num % 1000) + 1000 * i
                if my_list[alt] > cnt + 1:
                    heap.append((cnt + 1, alt))

# 소수 배열 생성 소수는 10001, 나머지는 -1
for i in range(2, 10000):
    if array[i] == 10001:
        for j in range(2*i, 10000, i):
            array[j] = -1

for _ in range(N):
    start, end = map(int, input().strip().split())
    ans = 'Impossible'
    do(start)
    print(ans)

# 소수 문제와 최단 경로 그래프 탐색을 응용한 문제이다.
# 처음에 힙을 떠올리지 못해서 조금 헤맸는데, 풀리더라