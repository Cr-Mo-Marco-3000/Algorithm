def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], n-1):
            result.append([elem] + rest)
    return result

print(combination([0, 1, 2, 3], 2))