# Phase 9. 동적 프로그래밍 (DP) - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase09_problems.md)

---

## 1. DP란?

> 큰 문제를 작은 문제로 나누고, 작은 문제의 결과를 저장(메모)해서 재사용.
> 같은 계산을 반복하지 않으므로 속도가 빠름!

### DP가 가능한 조건
1. **최적 부분 구조**: 큰 문제의 답이 작은 문제의 답으로 구성됨
2. **중복 부분 문제**: 같은 작은 문제가 반복해서 등장

### DP 풀이 4단계
1. dp[i]의 **정의**를 세운다
2. **점화식**을 찾는다 (dp[i] = ?)
3. **초기값**을 설정한다
4. **답**을 구한다

---

## 2. Bottom-up (반복문) - 가장 많이 사용

```python
# 피보나치
dp = [0] * (n + 1)
dp[1] = 1
# dp[2] = 1  (필요시)

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
```

### 예제: 1로 만들기 (BOJ 1463)
```python
# dp[i] = i를 1로 만드는 최소 연산 횟수
# 연산: ÷3, ÷2, -1

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1              # -1 하는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
```

---

## 3. Top-down (재귀 + 메모이제이션)

```python
from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 4. 대표 DP 유형

### 타일링
```python
# 2×n 직사각형을 1×2, 2×1 타일로 채우는 경우의 수
# dp[i] = dp[i-1] + dp[i-2]
dp[1] = 1  # |
dp[2] = 2  # || 또는 =
```

### 계단 오르기 (조건부 DP)
```python
# 1칸 또는 2칸씩 오를 수 있고, 연속 3칸 불가
# dp[i] = max(dp[i-2] + stair[i],
#              dp[i-3] + stair[i-1] + stair[i])
```

### 2차원 DP (경로/삼각형)
```python
# 정수 삼각형: 위에서 아래로 최대 합 경로
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + tri[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
```

### LIS (가장 긴 증가하는 부분 수열)
```python
# O(n²) 풀이
# dp[i] = arr[i]로 끝나는 LIS의 길이
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
```

### 배낭 문제 (0/1 Knapsack)
```python
# dp[i] = 무게 i일 때 최대 가치
dp = [0] * (k + 1)   # k = 배낭 용량

for w, v in items:    # 무게, 가치
    for j in range(k, w - 1, -1):   # 역순 순회!
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[k])
```

### LCS (최장 공통 부분수열)
```python
# dp[i][j] = s1[:i]와 s2[:j]의 LCS 길이
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```
