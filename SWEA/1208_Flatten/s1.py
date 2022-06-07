import sys

sys.stdin = open("input.txt")



for tc in range(1, 11):
    box_count = [0] * 101
    # 첫 번째 케이스의 경우, limit는 834이다.
    Limit = int(input())
    box_list = list(map(int, input().split()))

    for i in box_list:
        box_count[i] +=1
    # print(box_count)

    left = 0
    right = 100
    dump = 0
    while dump < Limit:
        if box_count[left] > 0:                     # left에도 숫자가 있고
            if box_count[right] > 0:                # right에도 숫자가 있는 경우
                box_count[left] -= 1                # 즉 현재 인덱스가 머무르는 곳이 최고높이와 최저높이라면,
                box_count[left + 1] += 1
                box_count[right] -= 1
                box_count[right-1] += 1
                dump += 1                           # 가장 높은 박스에서 낮은 박스로 옮겨주고 덤프횟수 +1을 해준다.
                if box_count[right] == 0:           # Caution!
                    right -= 1                      # 만약 박스에서 옮기고 나서 어떤 높이를 가진 박스 개수가 0이 되었을 때,
                if box_count[left] == 0:            # dump가 Limit를 넘어버리면 인덱스가 옮겨지지 않고 출력되어 버린다.
                    left += 1                       # 따라서 그런 경우에는 직접 인덱스를 옮겨줘야 한다.

            elif box_count[right] == 0:
                right -= 1
        elif box_count[left] == 0:                  # 만약 아니라면, 왼쪽과 오른쪽을 한 단계씩 좁혀서 다시 시행한다.
            left += 1
    ans = right - left

    print('#{} {}'.format(tc, ans))

