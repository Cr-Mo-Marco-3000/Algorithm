N = int(input().strip())

Array = tuple(map(int, input().strip().split()))

num = int(input().strip())

yak = 0
bae = 0

for i in range(N):
    test = Array[i]
    if not num % test:
        yak += test
    if not test % num:
        bae += test

print(yak)
print(bae)