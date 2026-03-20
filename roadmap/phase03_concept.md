# Phase 3. 리스트 완전 정복 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase03_problems.md)

---

## 1. 리스트 생성

```python
# 빈 리스트
a = []
a = list()

# 초기값
a = [1, 2, 3, 4, 5]
a = [0] * 10                    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = list(range(1, 6))           # [1, 2, 3, 4, 5]
a = list(range(0, 10, 2))       # [0, 2, 4, 6, 8]

# 입력으로 리스트 만들기
n = int(input())
data = [int(input()) for _ in range(n)]          # n줄, 줄마다 하나
nums = list(map(int, input().split()))           # 한 줄에 여러 개
```

### 2차원 리스트 (매우 중요!)
```python
# 올바른 생성
board = [[0] * 5 for _ in range(3)]
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]

# !!주의!! 잘못된 생성
board = [[0] * 5] * 3   # 같은 리스트를 3번 참조!
board[0][0] = 1          # board[1][0], board[2][0]도 1이 됨!

# 왜?
# [[0]*5] * 3은 같은 메모리를 가리키는 복사본
# for _ in range(3)은 매번 새로운 리스트를 만듦

# 입력으로 2차원 리스트
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
```

---

## 2. 인덱싱 & 슬라이싱

```python
a = [10, 20, 30, 40, 50]
#     0   1   2   3   4     (양수 인덱스)
#    -5  -4  -3  -2  -1     (음수 인덱스)

# 인덱싱
a[0]     # 10 (첫 번째)
a[2]     # 30
a[-1]    # 50 (마지막)
a[-2]    # 40

# 슬라이싱 [start:end:step]  (end는 미포함!)
a[1:4]   # [20, 30, 40]
a[:3]    # [10, 20, 30]      (처음~2)
a[2:]    # [30, 40, 50]      (2~끝)
a[::2]   # [10, 30, 50]      (2칸씩 건너뛰기)
a[::-1]  # [50, 40, 30, 20, 10]  (뒤집기)

# 슬라이싱으로 값 바꾸기
a[1:3] = [99, 88]   # [10, 99, 88, 40, 50]
```

---

## 3. 리스트 메서드 총정리

### 추가
```python
a = [1, 2, 3]

a.append(4)           # [1, 2, 3, 4]       끝에 추가 O(1)
a.insert(1, 99)       # [1, 99, 2, 3, 4]   인덱스 1에 삽입 O(n)
a.extend([5, 6])      # [1, 99, 2, 3, 4, 5, 6]  이어붙이기
a + [7, 8]            # 새 리스트 반환 (원본 유지)
a += [7, 8]           # extend와 같음
```

### 삭제
```python
a = [1, 2, 3, 4, 5, 3]

a.pop()        # 5 반환, [1, 2, 3, 4, 3]     마지막 제거 O(1)
a.pop(0)       # 1 반환, [2, 3, 4, 3]         인덱스 0 제거 O(n) 느림!
a.remove(3)    # [2, 4, 3]                     값 3을 첫 번째만 제거
del a[0]       # [4, 3]                        인덱스로 삭제
a.clear()      # []                            전부 삭제
```

### 검색
```python
a = [3, 1, 4, 1, 5, 9]

a.index(4)      # 2         값 4의 인덱스 (없으면 에러!)
a.index(1, 2)   # 3         인덱스 2부터 찾기
a.count(1)      # 2         값 1의 개수
4 in a          # True      포함 여부 O(n)
7 not in a      # True
```

### 정렬
```python
a = [3, 1, 4, 1, 5]

# 원본을 바꾸는 정렬
a.sort()                     # [1, 1, 3, 4, 5]  오름차순
a.sort(reverse=True)         # [5, 4, 3, 1, 1]  내림차순

# 원본 유지, 새 리스트 반환
b = sorted(a)                # a는 그대로, b만 정렬됨
b = sorted(a, reverse=True)

# 뒤집기
a.reverse()                  # [1, 1, 3, 4, 5] → [5, 4, 3, 1, 1]
b = list(reversed(a))        # 원본 유지 버전
```

### 유용한 내장함수
```python
a = [3, 1, 4, 1, 5]

len(a)          # 5       길이
sum(a)          # 14      합계
min(a)          # 1       최솟값
max(a)          # 5       최댓값
abs(-5)         # 5       절댓값

# 합치기
all([True, True, False])   # False  (전부 True?)
any([True, True, False])   # True   (하나라도 True?)

# zip: 여러 리스트 묶기
a = [1, 2, 3]
b = ['a', 'b', 'c']
list(zip(a, b))    # [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

## 4. 리스트 컴프리헨션

```python
# 기본 형태: [표현식 for 변수 in 반복가능]
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건 필터링: [표현식 for 변수 in 반복가능 if 조건]
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# if-else 포함 (위치가 다름!)
signs = [x if x > 0 else 0 for x in [-3, -1, 0, 2, 4]]
# [0, 0, 0, 2, 4]

# 문자열 변환
nums = [int(x) for x in input().split()]

# 2차원 평탄화
board = [[1,2], [3,4], [5,6]]
flat = [x for row in board for x in row]
# [1, 2, 3, 4, 5, 6]

# 위 코드는 아래와 같음:
flat = []
for row in board:
    for x in row:
        flat.append(x)
```

---

## 5. 2차원 리스트 다루기

```python
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
n = 3  # 행 수
m = 3  # 열 수

# 전체 순회 (행 우선)
for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()
# 1 2 3
# 4 5 6
# 7 8 9

# 행(가로) 합계
for i in range(n):
    print(sum(board[i]))       # 6, 15, 24

# 열(세로) 합계
for j in range(m):
    col_sum = sum(board[i][j] for i in range(n))
    print(col_sum)             # 12, 15, 18

# 대각선
diag1 = [board[i][i] for i in range(n)]           # [1, 5, 9] 주대각선
diag2 = [board[i][n-1-i] for i in range(n)]       # [3, 5, 7] 부대각선

# 전치 (행↔열 교환)
transposed = [[board[j][i] for j in range(n)] for i in range(m)]
# [[1,4,7], [2,5,8], [3,6,9]]

# 90도 시계방향 회전
rotated = [[board[n-1-j][i] for j in range(n)] for i in range(m)]
# [[7,4,1], [8,5,2], [9,6,3]]

# 2차원 배열 마킹 (색종이 문제 등)
paper = [[0] * 100 for _ in range(100)]
# (x, y)부터 10x10 칸 마킹
x, y = 3, 5
for i in range(x, x + 10):
    for j in range(y, y + 10):
        paper[i][j] = 1
# 마킹된 칸 수 세기
total = sum(paper[i][j] for i in range(100) for j in range(100))
```

---

## 6. 자주 쓰는 패턴 모음

```python
# 패턴 1: 최댓값의 인덱스 찾기
a = [3, 7, 2, 9, 4]
max_val = max(a)
max_idx = a.index(max_val)    # 3

# 패턴 2: 리스트 중복 제거 (순서 유지)
a = [3, 1, 4, 1, 5, 3]
seen = set()
unique = []
for x in a:
    if x not in seen:
        seen.add(x)
        unique.append(x)
# [3, 1, 4, 5]

# 패턴 3: 두 리스트 비교
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a == b              # True (내용 비교)

# 패턴 4: 리스트 복사 (주의!)
a = [1, 2, 3]
b = a               # 같은 리스트를 가리킴! a 바꾸면 b도 바뀜!
b = a[:]             # 얕은 복사 (1차원은 OK)
b = a.copy()         # 위와 동일
import copy
b = copy.deepcopy(a) # 깊은 복사 (2차원 이상은 이걸 사용)

# 패턴 5: 빈도 카운팅 (리스트 활용)
nums = [1, 3, 2, 3, 1, 1, 4]
count = [0] * 10     # 0~9까지 카운팅
for n in nums:
    count[n] += 1
# count = [0, 3, 1, 2, 1, 0, 0, 0, 0, 0]
#          0  1  2  3  4
```
