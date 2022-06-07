import sys

sys.stdin = open('sample_input.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def do():
    global temp
    if len(temp) == 6:
        temp2 = temp[:]
        moves.append(temp2)
        return
    else:
        for i in range(4):
            temp.append(i)
            do()
            temp.pop()

def do2(sr, sc):
    for move in moves:
        number = g[sr][sc]
        k = 0
        r = sr
        c = sc
        while k < 6:
            nr, nc = r + dr[move[k]], c + dc[move[k]]
            if 0 <= nr < 4 and 0 <= nc < 4:
                number = number * 10 + g[nr][nc]
                r, c = nr, nc
                k += 1
            else:
                break
        else:
            my_set.add(number)


T = int(input())
for tc in range(1, T+1):
    temp = []
    moves = []

    my_set = set()
    g = [list(map(int, input().split())) for _ in range(4)]
    

    do()                         # 모든 움직임의 경우의 수를 만들어 주는 함수
    # print(moves)
    for i in range(4):
        for j in range(4):
            do2(i, j)            # 어떤 좌표에서, 움직임을 넣어서 숫자를 구하는 함수

    print(f'#{tc} {len(my_set)}')
