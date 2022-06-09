N = int(input())

Stack = []

for i in range(N):
    order = tuple(map(str, input().strip().split()))
    if order[0] == 'i':
        Stack.append(order[1])
    elif order[0] == 'c':
        print(len(Stack))
    elif order[0] == 'o':
        if not Stack:
            print("empty")
        else:
            print(Stack.pop())