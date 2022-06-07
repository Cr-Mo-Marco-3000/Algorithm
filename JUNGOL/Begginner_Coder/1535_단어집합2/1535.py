my_list = []
my_set = set()

string = ''
while True:
    string = list(map(str, input().strip().split()))
    if string == ["END"]:
        break
    for i in string:
        if not (i in my_set):
            my_set.add(i)
            my_list.append(i)
    print(*my_list)

