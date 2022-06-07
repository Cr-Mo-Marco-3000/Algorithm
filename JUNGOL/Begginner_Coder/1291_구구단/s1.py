s, e = map(int, input().split())

while True:
    if not (2 <= s <= 9) or not (2 <= e <= 9):
        print('INPUT ERROR!')
        s, e = map(int, input().split())
    else:
        break

string_list = []

for i in range(1, 10):
    temp_string = ''
    if s <= e:
        for j in range(s, e+1):
            if j == e:
                if (j * i) // 10:
                    temp_string += f'{j} * {i} = {j * i}'
                else:
                    temp_string += f'{j} * {i} =  {j * i}'
            else:
                if (j * i) // 10:
                    temp_string += f'{j} * {i} = {j * i}   '
                else:
                    temp_string += f'{j} * {i} =  {j * i}   '
        string_list.append(temp_string)
    else:
        for j in range(s, e-1, -1):
            if j == e:
                if (j * i) // 10:
                    temp_string += f'{j} * {i} = {j * i}'
                else:
                    temp_string += f'{j} * {i} =  {j * i}'
            else:
                if (j * i) // 10:
                    temp_string += f'{j} * {i} = {j * i}   '
                else:
                    temp_string += f'{j} * {i} =  {j * i}   '
        string_list.append(temp_string)

for k in string_list:
    print(k)

# 쉽게 접근했다 피를 본 문제
# 문제를 천천히 잘 읽고, 모든 경우의 수를 고려해야 한다.
# 코드가 짧은 사람들은 어떻게 했는지 모르겠다.