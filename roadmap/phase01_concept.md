# Phase 1. Python 기초 & 입출력 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase01_problems.md)

---

## 1. 입출력

### 기본 입력
```python
a = int(input())                        # 정수 하나 입력
a, b = map(int, input().split())        # 한 줄에 정수 두 개
nums = list(map(int, input().split()))  # 한 줄에 여러 정수 → 리스트
s = input()                             # 문자열 한 줄
```

### 빠른 입력 (코테 필수!)
```python
import sys
input = sys.stdin.readline
# 이유: input()은 느림. 입력이 10만 줄 이상이면 시간초과 날 수 있음
# 주의: readline()은 끝에 '\n'이 붙으므로 문자열이면 .strip() 필요
name = input().strip()
```

### 여러 줄 입력 패턴
```python
# 패턴 1: N줄 입력
n = int(input())
for _ in range(n):
    x = int(input())

# 패턴 2: N줄을 리스트로
n = int(input())
data = [int(input()) for _ in range(n)]

# 패턴 3: EOF까지 입력 (몇 줄인지 모를 때)
import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

# 패턴 4: try/except로 EOF
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
```

### 출력
```python
print(a)                    # 기본 출력
print(a, b)                 # 공백으로 구분: "1 2"
print(a, b, sep='\n')       # 줄바꿈으로 구분
print(a, end='')            # 줄바꿈 없이 출력
print(f"{a} + {b} = {a+b}") # f-string (가장 편한 포매팅)

# 리스트 출력
nums = [1, 2, 3, 4, 5]
print(*nums)                # "1 2 3 4 5" (언패킹)
print(' '.join(map(str, nums)))  # 같은 결과
```

---

## 2. 자료형

### 숫자형
```python
a = 10          # int (정수) - Python은 크기 제한 없음!
b = 3.14        # float (실수) - 소수점 오차 주의
c = True        # bool - True는 1, False는 0으로 취급

# 형변환
int("123")      # 123   (문자열 → 정수)
int(3.7)        # 3     (소수점 버림, 반올림 아님!)
float("3.14")   # 3.14  (문자열 → 실수)
str(123)        # "123" (정수 → 문자열)
bool(0)         # False (0, "", [], {} 등은 False)
bool(1)         # True  (나머지는 True)
```

### 연산자
```python
# 산술 연산자
10 + 3    # 13    덧셈
10 - 3    # 7     뺄셈
10 * 3    # 30    곱셈
10 / 3    # 3.333 나눗셈 (항상 float!)
10 // 3   # 3     몫 (정수 나눗셈, 소수점 버림)
10 % 3    # 1     나머지
2 ** 10   # 1024  거듭제곱

# 자주 쓰는 활용
n = 12345
n % 10     # 5     (일의 자리)
n // 10    # 1234  (일의 자리 제거)
n % 100    # 45    (뒤 두 자리)
n // 100   # 123   (뒤 두 자리 제거)

# 비교 연산자: ==, !=, <, >, <=, >=
# 논리 연산자: and, or, not
# 멤버십 연산자: in, not in
3 in [1, 2, 3]     # True
'a' in 'apple'     # True
```

---

## 3. 조건문

```python
# 기본 구조
if 조건1:
    실행문1
elif 조건2:
    실행문2
else:
    실행문3

# 예시: 학점 판별
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 삼항 연산자 (한 줄 조건)
result = "짝수" if n % 2 == 0 else "홀수"
bigger = a if a > b else b

# 여러 조건 결합
if 1 <= n <= 100:           # 범위 확인 (파이썬만 가능!)
    print("1~100 사이")

if a > 0 and b > 0:         # 둘 다 양수
    print("둘 다 양수")

if a == 0 or b == 0:        # 하나라도 0
    print("0이 있다")
```

---

## 4. 반복문

### for문
```python
# range(끝): 0부터 끝-1까지
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

# range(시작, 끝): 시작부터 끝-1까지
for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i)

# range(시작, 끝, 증가값)
for i in range(0, 10, 2):    # 0, 2, 4, 6, 8 (짝수)
for i in range(10, 0, -1):   # 10, 9, 8, ..., 1 (역순)
for i in range(5, 0, -1):    # 5, 4, 3, 2, 1

# 리스트 순회
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 인덱스와 값 동시에 (enumerate)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

### while문
```python
# 조건이 True인 동안 반복
n = 10
while n > 0:
    print(n)
    n -= 1       # n = n - 1

# 무한루프 + break
while True:
    s = input()
    if s == "quit":
        break    # 반복 즉시 종료
    print(s)
```

### break, continue
```python
# break: 반복문 완전히 탈출
for i in range(10):
    if i == 5:
        break        # i=5에서 반복 종료
    print(i)         # 0, 1, 2, 3, 4

# continue: 이번 회차만 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue     # 짝수면 건너뜀
    print(i)         # 1, 3, 5, 7, 9
```

### 중첩 반복문 (별 찍기 원리)
```python
# 별 찍기 원리
# n=5일 때:
# *
# **
# ***
# ****
# *****

n = 5
for i in range(1, n + 1):     # i = 1, 2, 3, 4, 5
    print('*' * i)             # 문자열 * 숫자 = 반복!

# 오른쪽 정렬 별
#     *
#    **
#   ***
#  ****
# *****
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

# 피라미드
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2*i - 1))
```

---

## 5. 리스트 맛보기

> 리스트 상세는 Phase 3에서 다룹니다. 여기선 기본만!

```python
# 리스트 생성
a = [1, 2, 3, 4, 5]
a = []                          # 빈 리스트

# 기본 연산
len(a)                          # 길이
a.append(6)                     # 끝에 추가
a[0]                            # 첫 번째 원소
a[-1]                           # 마지막 원소

# 유용한 내장함수
sum([1, 2, 3, 4, 5])           # 15 (합계)
min([3, 1, 4, 1, 5])           # 1  (최솟값)
max([3, 1, 4, 1, 5])           # 5  (최댓값)

# 입력 → 리스트
nums = list(map(int, input().split()))
```
