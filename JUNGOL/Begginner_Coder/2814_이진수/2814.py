string = input()
string = list(map(str, string))
string.reverse()
total = 0
for i in range(len(string)):
    total += int(string[i]) * 2 ** i
print(total)
