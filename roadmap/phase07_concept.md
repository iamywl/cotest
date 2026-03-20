# Phase 7. 수학 & 브루트포스 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase07_problems.md)

---

## 1. 소수 (Prime Number)

### 소수 판별 O(√n)
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # √n까지만 확인!
        if n % i == 0:
            return False
    return True

# 왜 √n까지?
# 12 = 2×6 = 3×4 = 4×3 = 6×2
# 약수 쌍 중 하나는 반드시 √12(≈3.46) 이하
```

### 에라토스테네스의 체 (범위 내 모든 소수)
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i의 배수를 전부 제거 (i*i부터 시작!)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

primes = sieve(100)  # [2, 3, 5, 7, 11, 13, ..., 97]
```

---

## 2. 최대공약수 & 최소공배수

```python
import math

# 최대공약수 (GCD)
math.gcd(12, 8)       # 4

# 유클리드 호제법 (직접 구현)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 (LCM)
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 여러 수의 GCD/LCM
from functools import reduce
nums = [12, 18, 24]
reduce(math.gcd, nums)           # 6
reduce(lcm, nums)                # 72
```

---

## 3. 브루트포스 (완전 탐색)

> 가능한 모든 경우를 다 해보는 것. 단순하지만 확실한 방법!
> N이 작으면 (≤20~30) 브루트포스로 해결 가능.

```python
# 예: 세 수의 합이 target인 조합 찾기
nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10

# 3중 반복
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                print(nums[i], nums[j], nums[k])
```

### itertools 활용
```python
from itertools import permutations, combinations, product

# 순열 (순서 O, 중복 X): nPr
list(permutations([1,2,3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# 조합 (순서 X, 중복 X): nCr
list(combinations([1,2,3], 2))
# [(1,2), (1,3), (2,3)]

# 중복 순열 (순서 O, 중복 O)
list(product([1,2,3], repeat=2))
# [(1,1), (1,2), (1,3), (2,1), (2,2), ...]

# 중복 조합 (순서 X, 중복 O)
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]
```

---

## 4. 재귀 (Recursion)

```python
# 재귀: 함수가 자기 자신을 호출
# 반드시 종료 조건(base case)이 있어야 함!

# 팩토리얼
def factorial(n):
    if n <= 1:          # 종료 조건
        return 1
    return n * factorial(n - 1)

# 피보나치 (비효율적! → DP로 개선 필요)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# 재귀 깊이 제한 해제 (Python 기본 1000)
import sys
sys.setrecursionlimit(10**6)
```

### 백트래킹 (N과 M 시리즈)
```python
# 1~N에서 M개를 고르는 순열 (BOJ 15649)
def backtrack(depth, selected):
    if depth == m:
        print(*selected)
        return

    for i in range(1, n + 1):
        if i not in selected:           # 아직 안 쓴 수만
            selected.append(i)
            backtrack(depth + 1, selected)
            selected.pop()              # 되돌리기!

n, m = map(int, input().split())
backtrack(0, [])
```
