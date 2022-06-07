import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 도시 크기 N, 한 가구당 지불비용 M
    N, M = map(int, input().split())
    # 집의 개수 cnt
    cnt = 0
    # 그래프 g
    g = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        cnt += temp.count(1)
        g.append(temp)

    # 탐색해야 할 범위
    my_list = []
    for a in range(1, 2*N+1):
        if M * cnt >= a * a + (a-1) * (a-1):
            my_list.append(a)
        else:
            break
    # my_list = [1, 2, 3, 4]
    ans = 0
    for x in my_list:
        for i in range(N):
            for j in range(N):
                total = 0
                # 행 순환
                for k in range(0-(x-1), 0 + x):
                    for l in range(abs(k)-(x-1), x - abs(k)):
                        if 0 <= i+k < N and 0 <= j+l < N and g[i+k][j+l] == 1:
                            total += 1
                if total * M >= x*x + (x-1)*(x-1):
                    if total > ans:
                        ans = total




    print('#{} {}'.format(tc, ans))

