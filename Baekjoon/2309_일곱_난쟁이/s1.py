import sys

sys.stdin = open('input.txt')


my_list = []
for i in range(9):
    my_list.append(int(input()))
# 아홉 난쟁이의 키가 모두 다르다
# 부분집합 문제로 풀라는거지?
ans_list = []
for i in range(1 << 9):
    ans_list = []
    for j in range(9):
        if i & (1 << j):
            ans_list.append(my_list[j])
    if len(ans_list) == 7 and sum(ans_list) == 100:
        ans_list.sort()
        for i in ans_list:
            print(i)
        break
