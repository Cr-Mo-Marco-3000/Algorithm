# '''
# 3
# 1 2 3
# 1 3 2
# '''
# from collections import deque
#
# def do(v):
#     if g[v]:
#     # if v <= n:
#         do(g[v][0])
#         g[v][1] = in_list.popleft()
#         do(g[v][2])
#
# def do_2(v):
#     if v <= n:
#         print(g[v][1], end=' ')
#         do_2(g[v][0])
#         do_2(g[v][2])
#
#
# n = int(input())
#
# g = deque([[0, 0, 0]])
#
# for i in range(1, n + 1):
#     g.append([2*i, 0, 2*i + 1])
#
# # 걍 완전 이진 트리로 순서 만들고, 배치하면 되겠네
# in_list = deque(map(int, input().split()))
# post_list = deque(map(int, input().split()))
#
# do(1)
# print(g)
# do_2(1)

# 일단 보류