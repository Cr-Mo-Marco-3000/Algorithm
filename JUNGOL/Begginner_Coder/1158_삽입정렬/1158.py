N = int(input())

array = list(map(int, input().strip().split()))

for i in range(1, N):
    value = array.pop(i)
    if value < array[0]:
        array.insert(0, value)
    elif value > array[i-1]:
        array.insert(i)
    else:
        for j in range(0, i):

