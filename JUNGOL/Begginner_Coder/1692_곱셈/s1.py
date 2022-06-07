n1 = int(input())
n2 = input()
ans = 0
for i in range(3):
    num = int(n2[3-1-i])
    num = num*n1
    ans += num * 10 ** i
    print(num)
print(ans)

# 이 문제 역시 단순해 보이지만 인덱스 컨트롤과 조건이 꽤나 까다롭고 귀찮다.
# 다행히 오답은 나오지 않았다.