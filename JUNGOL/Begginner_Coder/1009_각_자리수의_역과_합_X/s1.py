
string = input().rstrip()

while string != '0':
    number = int(string)
    total = 0
    N = len(string)
    for i in range(N):
        print(string[N-1-i], end='')
        total += int(string[i])
    print(' ', end='')
    print(total)
    string = input().rstrip()
