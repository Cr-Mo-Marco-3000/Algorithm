import sys

def do2(flag, target):
    sum = -1
    cnt = flag
    while cnt < N and array[cnt] == target:
        sum += 1
        cnt += 1
    cnt = flag
    while cnt >= 0 and array[cnt] == target:
        sum += 1
        cnt -= 1
    return sum


def do(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        num = array[mid]
        if num == target:
            return do2(mid, target)
        elif num > target:
            right = mid - 1
        elif num < target:
            left = mid + 1
    return 0

input = sys.stdin.readline

N = int(input().strip())

array = list(map(int, input().strip().split()))

array.sort()

my_set = set(array)

my_dict = {}

for i in range(array):
    my_dict.setdefault(array[i], 1)

M = int(input().strip())
array2 = list(map(int, input().strip().split()))
for i in array2:
    print(do(0, N-1, i), end=' ')