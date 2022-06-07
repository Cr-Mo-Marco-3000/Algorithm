import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 1001
    for _ in range(N):
        kind, start, end = map(int, input().split())
        if kind == 1:
            for i in range(start, end+1):
                counts[i] += 1
        elif kind == 2:
            if not start % 2:
                i = start
                while i <= end:
                    counts[i] += 1
                    i += 2
                if end % 2:
                    counts[end] += 1
            if start % 2:
                i = start
                while i <= end:
                    counts[i] += 1
                    i += 2
                if not end % 2:
                    counts[end] += 1
        elif kind == 3:
            if not start % 2:
                counts[start] += 1
                for i in range(start + 1, end+1):
                    if not i % 4:
                        counts[i] += 1
                if end % 4:
                    counts[end] += 1
            elif start % 2:
                counts[start] += 1
                for i in range(start + 1, end + 1):
                    if not i % 3 and i % 10:
                        counts[i] += 1
                if end % 3 or not end % 10:
                    counts[end] += 1
    ans = max(counts)
    print('#{} {}'.format(tc, ans))

