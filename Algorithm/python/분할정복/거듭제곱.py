# N^K를 계산할 때, n을 k번 곱하면 k 번의 연산이 필요하다.
# K가 작다면 시간이 적게 걸리겠지만, 10^12같이 큰 경우에는 시간 초과가 발생한다.
# 분할 정복 거듭제곱을 이용한다면 연산을 크게 줄일 수 있을 것이다.
# 이 문제에서는 10^12번의 연산이 10000여번으로 줄어드는 결과를 가져온다.

# 1. 파이썬 거듭 제곱 모듈(소요시간 k에 비례)
def power1(n, k):
    return n ** k


# 2. n을 k번 곱하기
def power2(n, k):
    answer = 1
    for _ in range(k):
        answer *= n
    return answer


# 3. 재귀 활용 => 수가 커질 때를 대비해서 나머지를 고려하는 방법은 BOJ 1629번 또는 18291번 참고
def power3(n, k):
    if k == 1:
        return n
    else:
        m = power3(n, k // 2)
        if k % 2:
            return m * m * n
        else:
            return m * m

# 반복문 활용
def power4(n, k):
    answer = 1
    while k > 0:
        if k % 2:
            answer *= n
        n *= n
        k //= 2
    return answer



# 시간이 오래 걸린다.
# print(power1(10, 30))
# print(power2(10, 30))
# print(power3(10, 30))

# 씨발 반복문은 이해 못하겠다
print(power4(2, 10**9))