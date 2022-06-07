import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def do(num, start, end, flag):
    # 1은 오른쪽 2은 왼쪽
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return 1
        else:
            if num < arr[mid]:
                if flag == 2:
                    return 0
                elif (start == 0 and end == N-1) or flag == 1:
                    return do(num, start, mid-1, 2)
            if num > arr[mid]:
                if flag == 1:
                    return 0
                elif (start == 0 and end == N-1) or flag == 2:
                    return do(num, mid + 1, end, 1)

    return 0





for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 야이 정렬 좀 미리 해줘라
    arr.sort()
    search_list = list(map(int, input().split()))
    cnt = 0
    for i in search_list:
        cnt += do(i, 0, N - 1, 0)

    print('#{} {}'.format(tc, cnt))

