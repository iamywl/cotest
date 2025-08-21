import sys

def solve():
    S = "(()())"
    n = len(S)
    dp = [0] * n
    stack = []
    total_count = 0

    for i in range(n):
        if S[i] == '(':
            stack.append(i)
        elif S[i] == ')':
            if stack:
                j = stack.pop()
                count_at_prev = dp[j - 1] if j > 0 else 0
                dp[i] = 1 + count_at_prev
                total_count += dp[i]

    print(f"문자열 '{S}'의 올바른 괄호 부분 문자열의 총 개수: {total_count}")

def run_example(s_str):
    n = len(s_str)
    dp = [0] * n
    stack = []
    total_count = 0
    for i in range(n):
        if s_str[i] == '(':
            stack.append(i)
        elif s_str[i] == ')':
            if stack:
                j = stack.pop()
                count_at_prev = dp[j-1] if j > 0 else 0
                dp[i] = 1 + count_at_prev
                total_count += dp[i]
    return total_count

solve()

print(f"()() -> {run_example('()()')}")
print(f"(()) -> {run_example('(())')}")
print(f"(()))( -> {run_example('(()))(')}")