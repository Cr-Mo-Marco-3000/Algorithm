import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def sequence(my_string):
    my_string = list(map(str, my_string))
    is_sequence = True # 플래그 변수 선언
    while is_sequence == True:
        is_sequence = False # 들어가자마자 False로 바꾸고
        i = 0
        while i < len(my_string)-1: # 리스트를 훑다가
            if my_string[i] == my_string[i+1]:
                is_sequence = True # 연속 글자가 나오면, 그 글자들을 빼 주고
                my_string.pop(i)
                my_string.pop(i)
                continue # 그 자리부터 다시 순환한다.
            i += 1 
        if is_sequence == False: # 최종 순환에서 연속된 글자들이 없다면 순환을 완료했으므로 길이를 반환
            return len(my_string)

for tc in range(1, T+1):
    my_string = input()
    print(f'#{tc} {sequence(my_string)}')
