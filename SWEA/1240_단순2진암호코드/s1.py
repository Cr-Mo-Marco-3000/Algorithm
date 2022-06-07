import sys

sys.stdin = open('input.txt')

T = int(input())
# 암호들 입력
p_words = ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011')

for tc in range(1, T+1):
    # 각각 배열의 세로 크기 N, 배열의 가로크기 M이다
    N, M = map(int, input().split())
    string = []
    for i in range(N):
        temp = input()                                      # 어차피 암호문은 반복되므로, 한 줄만 봐도 된다.
        if string:                                          # 암호문을 받았을 경우, input()만 해준다.
            continue
        if '1' in temp:
            for j in range(M-1, -1, -1):                    # 암호들의 맨 뒷자리는 무조건 1이므로, 뒤에서부터 순환하며 판단
                if temp[j] == '1':
                    string = temp[j-55:j+1]                 # 만약 1을 발견하면, 앞쪽으로 56개의 글자를 저장 후
                    break                                   # 멈춰준다.

    ans_list = []
    for j in range(0, 8):                                   # 문자열을 7자씩 끊어서 저장해준다
        num = string[j * 7: (j + 1) * 7]
        for k in range(len(p_words)):                       # 족보 리스트를 순환하다 일치할 경우, ans_list에 append
            if p_words[k] == num:
                ans_list.append(k)
    ans = (ans_list[0] + ans_list[2] + ans_list[4] + ans_list[6]) * 3 + ans_list[1] + ans_list[3] + ans_list[5] + ans_list[7]
    if ans % 10:                                            # 10의 배수가 아닐 경우 0을 출력
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, sum(ans_list)))           # 10의 배수일 경우 암호의 합을 출력

