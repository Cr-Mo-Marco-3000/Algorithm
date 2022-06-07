import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    # 돌아가야 할 학생들의 수: N
    N = int(input())
    # 학생들의 움직임을 기록하기 위해, 카운트 배열을 만들어줬다.
    counts = [0] * 201
    for _ in range(N):
        student_move = list(map(int, input().split()))
        # 계산을 편리하게 해 주기 위해, 행을 하나로 통일해줬다.
        # 홀수면 // 2 + 1, 짝수면 // 2
        for i in range(2):
            if student_move[i] % 2: # 홀수
                student_move[i] = student_move[i] // 2 + 1
            elif not student_move[i] % 2: # 짝수
                student_move[i] = student_move[i] // 2
        # 만약 학생이 왼쪽부터 오른쪽으로 움직인다면, 범위를 지정해서 카운트 배열에 +를 해 준다.
        if student_move[0] <= student_move[1]:
            for j in range(student_move[0], student_move[1] + 1):
                counts[j] += 1
        # 반대라면, 반대로 해 준다.
        elif student_move[0] > student_move[1]:
            for j in range(student_move[1], student_move[0] + 1):
                counts[j] += 1

    time = max(counts)
    print('#{} {}'.format(tc, time))

