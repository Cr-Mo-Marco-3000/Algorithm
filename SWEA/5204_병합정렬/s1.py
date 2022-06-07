import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())

def merge(left, right):
    global cnt
    result = []
    left = deque(left)
    right = deque(right)
    if left[-1] > right[-1]:
        cnt += 1
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            elif left[0] > right[0]:
                result.append(right.popleft())
        else:
            if left:
                result.append(left.popleft())
            elif right:
                result.append(right.popleft())
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        length = len(arr)
        mid = length // 2
        left = arr[:mid]
        right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)
    print('#{} {} {}'.format(tc, ans[N//2], cnt))

