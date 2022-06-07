import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(w, t, cnt):
    global ans
    if t == M or w == N:
        if cnt > ans:
            ans = cnt
    else:
        for i in range(t, M):
            if w_list[w] <= t_list[i]:
                do(w + 1, i + 1, cnt + w_list[w])
                return
        else:
            do(w + 1, t, cnt)


for tc in range(1, T+1):
    # 컨테이너 수 N과 트럭 수 M이
    N, M = map(int, input().split())
    w_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    w_list.sort(reverse=True)
    t_list.sort(reverse=True)
    ans = 0
    do(0, 0, 0)
    print(f'#{tc} {ans}')