import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    g = [[0, 0, 0] for _ in range(N + 1)]
    # 중간값이 합(값)
    for _ in range(M):
        nod, num = map(int, input().split())
        g[nod][1] = num
    for i in range(N, 0, -1):
        g[i//2][1] += g[i][1]
    print('#{} {}'.format(tc, g[L][1]))

