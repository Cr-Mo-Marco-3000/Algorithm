# array = [0] * 100000001
#
# while True:
#     try:
#         n = int(input())
#     except ValueError or EOFError:
#         break
#     lowest = 100000001
#     highest = -1
#     N = n * 10000000
#     K = int(input().strip())
#     for i in range(K):
#         k = int(input().strip())
#         array[k] += 1
#         if k < lowest:
#             lowest = k
#         elif k > highest:
#             highest = k
#     for i in range(lowest, highest + 1):
#         j = N - i
#         if array[i] > 0 and array[j] > 0:
#             if i != j:
#                 print('yes', i, j)
#                 break
#             else:
#                 if array[i] > 1:
#                     print('yes', i, j)
#                     break
#     else:
#         print('danger')
#     for l in array:
#         if array[l]:
#             array[l] = 0

while True:
    try:
        n = int(input())
    except ValueError or EOFError:
        break
    N = n * 10000000
    array = []
    K = int(input())
    for i in range(K):
        k = int(input())
        array.append(k)
    array.sort()
    right = len(array) - 1
    left = 0
    while left <= right:
        v = array[left] + array[right]
        if v == N:
            if left != right:
                print('yes', array[left], array[right])
                break
            else:
                print('danger')
                break
        elif v > N:
            right -= 1
            continue
        elif v < N:
            left += 1
            continue
    else:
        print('danger')