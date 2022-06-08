# citations = [3, 0, 6, 1, 5]
citations = [0, 1, 2, 2, 4, 4, 6, 7, 8]

def solution(citations):
    citations.sort()
    N = len(citations)
    # [0, 1, 3, 5, 6]
    for i in range(N):
        # 우변부터 생각하자
        # 우변 => 전체 논문 수 중 현재 체크중인 숫자 - 1 를 제외한 논문의 수
        # 좌변 => 현재 남은 논문의 수(숫자 - 1) 중 인용 횟수가 가장 작은 논문의 인용수
        if citations[i] >= N - i:
            return N - i
    return 0

print(solution(citations))
