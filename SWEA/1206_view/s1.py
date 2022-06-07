import sys
# 이전과 다르게 2번에서는 조금 다르게 풀어볼 예정이다.
sys.stdin = open('input.txt')


for tc in range(1, 11): # 10번 반복한다.
    num_of_buildings = int(input()) # 빌딩의 개수이다.
    buildings_list = list(map(int, input().split())) # 숫자들을 빌딩 높이의 리스트로 만든다.
    total_ans = 0 # 출력할 부분을 선언과 초기화한다.
    for i in range(2, len(buildings_list) - 2): # 빌딩은 idx 2부터 -3까지 있다.
        five_list = sorted(buildings_list[i - 2 : i + 3 : 1]) # 해당 건물을 중심으로 5개의 빌딩을 나열한다.
        # .sort()는 None을 반환! 실수하지 말자.
        tallest_in_five = max(buildings_list[i - 2 : i + 3]) # max 함수를 썼는데, 굳이 쓸 필요 없을 것 같다.
        # five_list[-1]이 더 낫겠는데
        if buildings_list[i] == tallest_in_five: # 만약 범위 안에서 해당 건물이 가장 크다면,
            total_ans += buildings_list[i] - five_list[-2] # 그 해당 건물에서 두 번째로 큰 건물의 높이를 빼 준다.

    print(f"#{tc} {total_ans}")
