import sys
from itertools import permutations, combinations

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    my_list = list(range(N))
    food_set = list(combinations(my_list, N//2))
    ans = 100000
    for i in range(len(food_set)):
        a_set = list(food_set[i])
        b_set = []
        for j in my_list:
            if j not in a_set:
                b_set.append(j)

        maat_a = 0
        a_food_comb = list(permutations(a_set, 2))
        for k in a_food_comb:
            maat_a += g[k[0]][k[1]]

        maat_b = 0
        b_food_comb = list(permutations(b_set, 2))
        for l in b_food_comb:
            maat_b += g[l[0]][l[1]]

        if abs(maat_a - maat_b) < ans:
            ans = abs(maat_a - maat_b)

    print('#{} {}'.format(tc, ans))

