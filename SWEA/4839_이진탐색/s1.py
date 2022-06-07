import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    # P: 총 페이지, Pa: A가 찾을 페이지 Pb: B가 찾을 페이지
    P, Pa, Pb = map(int, input().split())
    start_a = start_b = 1
    end_a = end_b = P
    count_a = 0 # 횟수 초기화
    count_b = 0 # 횟수 초기화
    # A 케이스
    while start_a <= end_a:
        count_a += 1
        mid_a = (start_a + end_a) // 2
        if Pa == mid_a:
            break
        elif Pa > mid_a:
            start_a = mid_a
        elif Pa < mid_a:
            end_a = mid_a
    # B 케이스
    while start_b <= end_b:
        count_b += 1
        mid_b = (start_b + end_b) // 2
        if Pb == mid_b:
            break
        elif Pb > mid_b:
            start_b = mid_b
        elif Pb < mid_b:
            end_b = mid_b

    print(count_b,count_a)
    if count_a < count_b:
        print(f'#{tc} A')
    elif count_b < count_a:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')