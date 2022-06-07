import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def partition(arr, start, end):
    pivot = start
    left = start + 1
    right = end
    flag = 1
    while flag:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            flag = 0
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot], arr[right] = arr[right], arr[pivot]
    return right






def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot + 1, end)
    return arr

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print('#{} {}'.format(tc, arr[N//2]))

