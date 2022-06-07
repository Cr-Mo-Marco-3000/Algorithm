import sys

sys.stdin = open('test_input.txt', encoding="UTF8")
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 5065: illegal multibyte sequence
# encoding="UTF8"을 안 붙이면 뜬다.
T = 10

def searching(target, pattern, N, M):
    '''
    :param target:
    문자열
    :param pattern: 
    패턴
    :param N:
    문자열의 길이
    :param M:
    패턴의 길이
    :return:
    cnt 반환
    '''
    cnt = 0  # 문자열의 개수 초기화
    j = 0 # 패턴 탐색 인덱스
    i = 0
    while i < N - M + 1: # 인덱스를 끝까지 탐색: 경제적으로 for과 while문 같이 사용
        for j in range(M): # for else 문을 사용했다.
            if target[i+j] != pattern[j]: # 만약 중간에 글자가 다르다면
                break # 브레이크
        else: # 끝까지 같아준다면
            cnt += 1 # 개수 카운트에 추가해준다.
        i += 1
    return cnt

for tc in range(1, T+1):
    num = int(input())
    pattern = input()
    target = input()
    N = len(target)
    M = len(pattern)
    ans = searching(target, pattern, N, M)

    print('#{} {}'.format(tc, ans))

