import sys, collections
sys.stdin = open('sample_input.txt')
T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def do(level, cnt, line):
    global ans_line
    global ans_core
    if level == length:
        if cnt > ans_core:
            ans_core = cnt
            ans_line = line
        elif cnt == ans_core:
            if ans_line > line:
                ans_line = line
        return
    else:
        r, c = axios_list[level]
        # 맞닿아 있다면 그냥 pass => 선은 늘어나지 않고, 연결할 수 있는 액시오스만 하나 늘린다.
        if r == 0 or c == 0 or r == N-1 or c == N-1:
            do(level+1, cnt+1, line)
        else:
            # 사방 탐색
            for w in range(4):
                nr = r + dr[w]
                nc = c + dc[w]
                extend = 0
                backList = []
                while True:
                    if 0 <= nr < N and 0 <= nc < N and not g[nr][nc]:
                        backList.append((nr, nc))
                        g[nr][nc] = 2
                        extend += 1
                        nr = nr + dr[w]
                        nc = nc + dc[w]
                    elif not (0 <= nr < N) or not (0 <= nc < N):
                        do(level + 1, cnt+1, line + extend)
                        while backList:
                            br, bc = backList.pop()
                            g[br][bc] = 0
                        break
                    elif g[nr][nc]:
                        while backList:
                            br, bc = backList.pop()
                            g[br][bc] = 0
                        break
            else:
                do(level + 1, cnt, line)


for tc in range(1, T+1):
    g = []
    ans_core = 0
    ans_line = 0
    axios_list = []
    N = int(input())
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j]:
                axios_list.append((i, j))
        g.append(temp)
    length = len(axios_list)
    do(0, 0, 0)
    print(f'#{tc} {ans_line}')
