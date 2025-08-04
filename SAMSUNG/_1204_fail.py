def solve():
    tc_num = int(input())
    scores = list(map(int, input().split()))

    counts = [0] * 101

    for score in scores:
        counts[score] += 1

    max_count = -1
    mode_score = -1
    # 모두 다찾아보게 되므로 최대값이 아니다..?
    for score in range(100, -1, -1):
        if counts[score] >= max_count:
            max_count = counts[score]
            mode_score = score

    return f"#{tc_num} {mode_score}"

T = int(input())

for _ in range(T):
    print(solve())