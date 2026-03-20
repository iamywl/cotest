# Phase 10. 그리디 알고리즘 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase10_problems.md)

---

## 1. 그리디란?

> 매 순간 가장 좋아 보이는 선택을 하면 전체적으로도 최적이 되는 알고리즘.
> DP와 달리 이전 결과를 돌아보지 않고, 현재 최선만 선택.

### 그리디가 통하는 조건
- **탐욕적 선택 속성**: 지금 최선 = 전체 최선
- **최적 부분 구조**: 부분 문제의 최적해로 전체 최적해 구성

### 대표 예: 거스름돈
```python
# 500, 100, 50, 10원 동전으로 거스름돈 주기
# 큰 동전부터 최대한 사용 → 최소 동전 수
coins = [500, 100, 50, 10]
change = 1260
count = 0

for coin in coins:
    count += change // coin
    change %= coin

print(count)  # 6 (500×2 + 100×2 + 50×1 + 10×1)
```

---

## 2. 대표 유형

### 활동 선택 문제 (회의실 배정)
```python
# 끝나는 시간이 빠른 순으로 정렬 → 가능한 한 많이 선택
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end
```

### 정렬 후 탐욕
```python
# ATM: 작업 시간이 짧은 사람부터 처리
times = sorted(times)
total = 0
current = 0
for t in times:
    current += t
    total += current
```

---

## 3. 그리디 vs DP

| | 그리디 | DP |
|:---:|:---:|:---:|
| 접근 | 현재 최선 선택 | 모든 경우 고려 |
| 되돌아감 | X | O |
| 속도 | 빠름 | 상대적 느림 |
| 정당성 | 증명 필요 | 항상 최적 |
| 대표 문제 | 거스름돈, 회의실 | 배낭, LCS |

> 그리디인지 DP인지 판단이 어려우면, 반례를 찾아보자!
> 반례가 없으면 그리디, 있으면 DP.
