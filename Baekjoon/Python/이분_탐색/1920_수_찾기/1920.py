import sys

def do(left, right, target): # 반복으로 구현
    while left <= right:
        mid = (left + right) // 2
        num = array[mid]
        if num == target:
            return 1
        elif num > target:
            right = mid - 1
        elif num < target:
            left = mid + 1
    return 0

input = sys.stdin.readline

N = int(input().strip())
array = list(map(int, input().strip().split()))
array.sort() # 이진탐색은 sort()가 필수!

M = int(input().strip())

test = tuple(map(int, input().strip().split()))

for i in test:
    print(do(0, N-1, i))

# 최대 범위를 N으로 잡아주면, 찾는 수가 N보다 클 때, 인덱스 에러가 난다.