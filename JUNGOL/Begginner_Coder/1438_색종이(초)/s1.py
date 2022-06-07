import sys

input = sys.stdin.readline

g = [[0] * 101 for _ in range(101)]

T = int(input().rstrip())
cnt = 0
for _ in range(T):
    l, b = map(int, input().rstrip().split())
    for i in range(b, 10+b):
        for j in range(l, 10+l):
            if g[i][j] == 0:
                g[i][j] = 1
                cnt += 1
            else:
                continue
print(cnt)

# 주어진 모양은 1사분면이지만, 풀 때는 일반적인 그래프 형태로 풀었다.
# 보통 넓이 문제는 인덱스와 넓이를 어떻게 표현할 것인지 헷갈려서 그림을 그려 보아야 한다.
# 끝 값이 겹치지 않게 하려면, 예를 들어 밑변의 길이가 5부터 15까지라면,
# 그래프에 표시는 5부터 14까지 1로 해 놓아야 1로 표현된 밑변의 길이가 정확히 표시된다.

