import sys

N = int(sys.stdin.readline().rstrip())

try:
    # 분해합을 구할 때, 생성자는 어쨌든 자연수 N 보다 작을 것이다.
    # 1 씩 줄여가면서, 숫자 i의 각 자리수 + i 가 N이 나오는 것을 찾는다.
    for i in range(N, -1, -1):
        a = i
        num_list = []
        while a > 0:
            num_list.append(a % 10)
            a = a // 10
        if i + sum(num_list) == N:
            ans = i
    # 만약 값이 없을 경우에는, ans 값이 없어 오류가 날 것이므로, print(0)을 해 준다.
    print(ans)
except:
    print(0)