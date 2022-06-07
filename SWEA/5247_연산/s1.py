import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())

def do(N):
    global ans
    Q = deque([(N, 0)])
    while Q:
        num, cnt = Q.popleft()
        # visited[num] = 1                      # 여기서 체크해주면, 체킹이 늦어서 해당 숫자들이 큐에 더 들어가 시간초과가 뜬다.
        if cnt >= ans or num > 1000000 or num <= 0:
            continue
        if num == M:
            ans = cnt
        else:
            # if 0 < num < 1000000:             # 생각해보니 어차피 위에서 걸러진다.
                if not visited[num + 1]:
                    visited[num + 1] = 1
                    Q.append((num + 1, cnt + 1))
                if not visited[num - 1]:
                    visited[num - 1] = 1
                    Q.append((num - 1, cnt + 1))
                if not visited[num * 2]:
                    visited[num * 2] = 1
                    Q.append((num * 2, cnt + 1))
                if not visited[num - 10]:
                    visited[num - 10] = 1
                    Q.append((num - 10, cnt + 1))



for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 100000                                    # 1000000 까지만 만들어주면, 여튼 중간 연산 과정에서 * 2 때문에 더 큰 숫자가 나타나므로 런타임 에러가 뜬다.
    visited = [0] * 2000002
    do(N)
    print('#{} {}'.format(tc, ans))

