# Phase 6. 정렬 & 탐색 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase06_problems.md)

---

## 1. 정렬

### 기본 정렬
```python
a = [3, 1, 4, 1, 5]

# 원본 변경
a.sort()                      # [1, 1, 3, 4, 5]
a.sort(reverse=True)          # [5, 4, 3, 1, 1]

# 원본 유지 (새 리스트 반환)
b = sorted(a)
b = sorted(a, reverse=True)
```

### key를 이용한 커스텀 정렬 (핵심!)
```python
# lambda: 간단한 함수를 한 줄로
# key=lambda x: 기준   → 이 기준으로 정렬

# 문자열 길이순 정렬
words = ["banana", "apple", "fig", "cherry"]
words.sort(key=lambda x: len(x))
# ['fig', 'apple', 'banana', 'cherry']

# 두 번째 원소 기준
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
pairs.sort(key=lambda x: x[1])  # 알파벳순
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 다중 기준 정렬 (매우 자주 나옴!)
```python
# 튜플로 여러 기준 지정 → 앞에서부터 우선순위
students = [("김", 3, 90), ("이", 1, 85), ("박", 3, 70), ("최", 1, 85)]

# 1순위: 학년 오름차순, 2순위: 점수 내림차순, 3순위: 이름 오름차순
students.sort(key=lambda x: (x[1], -x[2], x[0]))
# [('이', 1, 85), ('최', 1, 85), ('김', 3, 90), ('박', 3, 70)]

# 주의: 문자열은 -를 못 붙임!
# 문자열 역순 정렬이 필요하면 → 별도 처리
```

### 안정 정렬 (Stable Sort)
```python
# Python의 sort()는 안정 정렬!
# → 같은 값이면 원래 순서 유지

# 이 성질을 활용: 2차 기준은 원래 순서(입력 순서) 그대로
data = [(21, "Junkyu"), (21, "Dohyun"), (20, "Sunyoung")]
data.sort(key=lambda x: x[0])
# [(20, 'Sunyoung'), (21, 'Junkyu'), (21, 'Dohyun')]
# 나이가 같은 21살은 입력 순서 유지!
```

---

## 2. 이진 탐색 (Binary Search)

> 정렬된 배열에서 O(log n)으로 값을 찾는 알고리즘.
> 반씩 줄여가면서 탐색 → 100만 개도 20번이면 찾음!

### 직접 구현
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:
            return mid          # 찾았다!
        elif arr[mid] < target:
            lo = mid + 1        # 오른쪽 반 탐색
        else:
            hi = mid - 1        # 왼쪽 반 탐색

    return -1                   # 못 찾음

# 사용
arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))    # 3 (인덱스)
print(binary_search(arr, 6))    # -1 (없음)
```

### bisect 모듈 (편리!)
```python
import bisect

a = [1, 3, 5, 7, 9]

# bisect_left: target이 들어갈 왼쪽 위치
bisect.bisect_left(a, 5)     # 2  (a[2]가 5)
bisect.bisect_left(a, 6)     # 3  (6이 들어갈 위치)
bisect.bisect_left(a, 0)     # 0  (맨 앞)

# bisect_right: target이 들어갈 오른쪽 위치
bisect.bisect_right(a, 5)    # 3  (5 다음 위치)

# 활용: 특정 범위의 개수
# a에서 2 이상 8 미만인 수의 개수
left = bisect.bisect_left(a, 2)    # 1
right = bisect.bisect_left(a, 8)   # 4
count = right - left                # 3 (3, 5, 7)
```

### 매개변수 탐색 (Parametric Search)
```python
# "최솟값의 최댓값" 또는 "조건을 만족하는 최대/최소" 문제에 사용
# 핵심: 정답을 이진 탐색으로 찾기!

# 예: BOJ 2805 나무 자르기
# H 높이로 잘라서 M미터 이상 가져갈 수 있는 최대 H는?

def solve():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    lo, hi = 0, max(trees)
    answer = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        # mid 높이로 잘랐을 때 얻는 나무 양
        total = sum(max(0, t - mid) for t in trees)

        if total >= m:      # 충분히 얻을 수 있으면
            answer = mid    # 이 높이 기록
            lo = mid + 1    # 더 높이 잘라보기
        else:               # 부족하면
            hi = mid - 1    # 더 낮게 잘라야 함
    print(answer)
```

---

## 3. 카운팅 정렬

```python
# 값의 범위가 작을 때 O(n)으로 정렬 가능
# 예: 0~10000 범위의 수 정렬

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001    # 0~10000

for _ in range(n):
    count[int(input())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
```
