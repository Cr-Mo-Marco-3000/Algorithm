import sys
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))

min_v = min(array)

for i in range(min_v, 0, -1):
    for j in array:
        if j % i:
            break
    else:
        biggest = i
        break

print(biggest, end=" ")

while len(array) != 1:
    a, b = array.pop(), array.pop()
    for i in range(min(a, b), 0, -1):
        if not a % i and not b % i:
            biggest = i
            break
    array.append(a * b // biggest)
print(array[0])