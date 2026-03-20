# Phase 5. 스택 & 큐 & 힙 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase05_problems.md)

---

## 1. 스택 (Stack) - 후입선출 (LIFO)

> 접시 쌓기와 같음. 마지막에 넣은 것을 먼저 꺼냄.

```python
# Python에서는 리스트로 스택 구현
stack = []

# push (넣기)
stack.append(1)    # [1]
stack.append(2)    # [1, 2]
stack.append(3)    # [1, 2, 3]

# pop (꺼내기) - 마지막 것이 나옴
stack.pop()        # 3 반환, stack = [1, 2]
stack.pop()        # 2 반환, stack = [1]

# top/peek (꺼내지 않고 확인)
stack[-1]          # 1

# empty 확인
len(stack) == 0    # False
not stack          # False  (빈 리스트는 False)

# size
len(stack)         # 1
```

### 스택 활용 1: 괄호 매칭 (가장 대표적!)
```python
def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':               # 여는 괄호 → push
            stack.append(ch)
        elif ch == ')':             # 닫는 괄호 → pop
            if not stack:           # 스택이 비었는데 닫는 괄호?
                return False        # → 짝이 안 맞음!
            stack.pop()
    return len(stack) == 0          # 스택이 비어야 모든 괄호 매칭 완료

print(is_valid("(())()"))   # True
print(is_valid("(()")  )    # False (여는 괄호 남음)
print(is_valid(")(")   )    # False (닫는 괄호가 먼저)
```

### 스택 활용 2: 여러 종류 괄호
```python
def is_valid_multi(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

### 스택 활용 3: 문자열 뒤집기 / 역순 처리
```python
# 스택으로 뒤집기
s = "Hello"
stack = list(s)             # ['H', 'e', 'l', 'l', 'o']
reversed_s = ""
while stack:
    reversed_s += stack.pop()
# "olleH"
```

---

## 2. 큐 (Queue) - 선입선출 (FIFO)

> 줄서기와 같음. 먼저 넣은 것을 먼저 꺼냄.

### 왜 deque를 써야 하나?
```python
# 리스트로 큐? → 느림!
queue = [1, 2, 3]
queue.pop(0)          # 1 반환, [2, 3]  → O(n)! 앞에꺼 빼면 전부 한 칸씩 이동

# deque로 큐! → 빠름!
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()       # 1 반환, deque([2, 3])  → O(1)!
```

### deque 사용법
```python
from collections import deque

q = deque()

# 뒤에 추가 (enqueue)
q.append(1)          # deque([1])
q.append(2)          # deque([1, 2])
q.append(3)          # deque([1, 2, 3])

# 앞에서 제거 (dequeue)
q.popleft()          # 1 반환, deque([2, 3])

# 앞 확인 (front)
q[0]                 # 2

# 뒤 확인 (back)
q[-1]                # 3

# deque 추가 기능 (양쪽 모두 O(1))
q.appendleft(0)      # 앞에 추가: deque([0, 2, 3])
q.pop()              # 뒤에서 제거: 3

# 회전
q = deque([1, 2, 3, 4, 5])
q.rotate(1)          # 오른쪽 회전: deque([5, 1, 2, 3, 4])
q.rotate(-1)         # 왼쪽 회전: deque([1, 2, 3, 4, 5])

# 길이, 포함 확인
len(q)               # 5
3 in q                # True
```

### 큐 활용: 카드 문제 (BOJ 2164)
```python
# 1~N 카드, 맨 위 버리고 다음 카드를 맨 아래로
from collections import deque
n = int(input())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()              # 맨 위 버리기
    q.append(q.popleft())   # 다음 카드를 맨 아래로

print(q[0])
```

---

## 3. 힙 / 우선순위 큐 (Heap)

> 항상 최솟값(또는 최댓값)을 O(log n)에 꺼낼 수 있는 자료구조.

### 최소 힙 (Python 기본)
```python
import heapq

heap = []

# push: 넣기
heapq.heappush(heap, 5)     # [5]
heapq.heappush(heap, 3)     # [3, 5]
heapq.heappush(heap, 7)     # [3, 5, 7]
heapq.heappush(heap, 1)     # [1, 3, 7, 5]

# pop: 최솟값 꺼내기
heapq.heappop(heap)         # 1 (항상 최솟값!)
heapq.heappop(heap)         # 3

# peek: 꺼내지 않고 최솟값 확인
heap[0]                      # 현재 최솟값

# 리스트 → 힙 변환
nums = [5, 3, 1, 4, 2]
heapq.heapify(nums)         # O(n)으로 힙 변환
```

### 최대 힙 (부호 반전 트릭)
```python
import heapq

# Python은 최소 힙만 지원! 최대 힙은 부호를 반전시켜 구현
heap = []

# 넣을 때 -를 붙이고
heapq.heappush(heap, -5)
heapq.heappush(heap, -3)
heapq.heappush(heap, -7)

# 꺼낼 때 -를 붙여서 원래 값 복원
val = -heapq.heappop(heap)  # 7 (최댓값!)
val = -heapq.heappop(heap)  # 5
```

### 절댓값 힙 (튜플 활용)
```python
import heapq

# 튜플을 넣으면 첫 번째 원소 기준으로 정렬됨!
heap = []
heapq.heappush(heap, (abs(-1), -1))   # (절댓값, 원래값)
heapq.heappush(heap, (abs(3), 3))
heapq.heappush(heap, (abs(-2), -2))

# 꺼내면 절댓값이 작은 순서
_, val = heapq.heappop(heap)           # val = -1
```

### 힙 활용: 정렬된 순서로 꺼내기
```python
import heapq

nums = [5, 3, 1, 4, 2]
heapq.heapify(nums)

result = []
while nums:
    result.append(heapq.heappop(nums))
# [1, 2, 3, 4, 5]  (힙 정렬)
```

---

## 비교 정리

| | 스택 (Stack) | 큐 (Queue) | 힙 (Heap) |
|:---:|:---:|:---:|:---:|
| 원리 | 후입선출 (LIFO) | 선입선출 (FIFO) | 우선순위 순 |
| 구현 | `list` | `deque` | `heapq` |
| 넣기 | `append()` | `append()` | `heappush()` |
| 빼기 | `pop()` | `popleft()` | `heappop()` |
| 확인 | `[-1]` | `[0]` | `[0]` |
| 빼기 시간 | O(1) | O(1) | O(log n) |
| 대표 문제 | 괄호 매칭 | BFS | 최솟값 반복 추출 |
