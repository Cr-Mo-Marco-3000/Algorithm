import sys 

sys.stdin = open("input.txt")

T = int(input()) # 테스트 케이스 값 입력

for tc in range(1, T+1): # 테스트 케이스를 T번만큼 반복한다.
    num_list = list(map(int, input().split())) # 받아들이는 수들을 쪼갠다. sum / len 쓰고 싶었는데 그냥 깡으로 풀었다.
    total = 0  # total 값을 선언 및 초기화한다.
    for n in num_list: # 리스트를 순환하며 토탈에 더해준다.
        total += n
    ans = round(total / 10) # round 함수를 써서 소수점 첫번째 자리에서 반올림 해 준다.
    print(f"#{tc} {ans}") # f-string을 써서 출력 양식을 완성했다.

