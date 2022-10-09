import sys
input = sys.stdin.readline
my_string = input().strip().split('-')
my_string2 = []
for i in my_string:
    temp = i.split('+')
    for j in range(len(temp)):
        temp2 = temp[j].lstrip('0')
        if temp2:
            temp[j] = int(temp2)
        else:
            temp[j] = 0
    my_string2.append(sum(temp))
ans = my_string2[0]
ans -= sum(my_string2[1:])
print(ans)

