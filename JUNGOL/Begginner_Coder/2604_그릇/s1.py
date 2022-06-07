from sys import stdin

my_str = stdin.readline().rstrip()
N = len(my_str)
rear = ''
total = 0
for i in range(N):
    char = my_str[i]
    if rear == char:
        total += 5
    else:
        total += 10
    rear = char
print(total)