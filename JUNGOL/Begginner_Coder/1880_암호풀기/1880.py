import sys

input = sys.stdin.readline

my_dict = {}

alpha = tuple(map(str, input().strip()))

cnt = 0
for char in alpha:
    my_dict[chr(97 + cnt)] = char
    big = chr(ord(char) - (97-65))
    my_dict[chr(65 + cnt)] = big
    cnt += 1

my_dict[" "] = " "

alpha2 = tuple(map(str, input().strip()))

for i in alpha2:
    print(my_dict[i], end="")

