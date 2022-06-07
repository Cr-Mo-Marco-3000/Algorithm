a, b = map(int, input().split())

check = min(a, b)
pull = max(a, b)

for i in range(check, 0, -1):
    if not pull % i and not check % i:
        biggest = i
        break

print(biggest)
print(a * b // biggest)