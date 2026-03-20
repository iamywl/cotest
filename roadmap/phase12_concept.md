# Phase 12. 고급 주제 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase12_problems.md)

---

## 1. 위상 정렬 (Topological Sort)

> 방향 그래프(DAG)에서 선후관계를 지키며 정렬.
> 선수과목, 빌드 순서 등.

```python
from collections import deque

def topological_sort():
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            indegree[j] += 1

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return result
```

---

## 2. 세그먼트 트리

> 구간 합, 구간 최소 등을 O(log n)에 쿼리/업데이트.

---

## 3. 분할 정복

> 문제를 반으로 나누어 해결 후 합치기.
> 병합 정렬, 거듭제곱, 히스토그램 등.

```python
# 빠른 거듭제곱 O(log n)
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = result * base % mod
        exp //= 2
        base = base * base % mod
    return result
```
