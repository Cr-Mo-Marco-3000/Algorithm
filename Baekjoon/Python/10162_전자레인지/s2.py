from sys import stdin

T = int(stdin.readline().rstrip())

# 각각 주어진 시간을, 초단위로 맞춘다.
A = 300
B = 60
C = 10

# # -1을 출력해야 하는 경우는 T에 1의 자리 숫자가 있는 경우이다.
if T < C or T % 10:
    print(-1)
else: # 1번 솔루션의 구간을 나누는 건 필요없었다.
    a = T // A
    b = (T % A) // B
    c = ((T % A) % B) // C
    print(f'{a} {b} {c}')
