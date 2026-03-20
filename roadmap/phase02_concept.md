# Phase 2. 문자열 처리 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase02_problems.md)

---

## 1. 문자열 기본

### 생성과 특성
```python
s = "Hello"
s = 'Hello'        # 큰따옴표, 작은따옴표 모두 가능
s = """여러 줄
문자열"""

# 핵심: 문자열은 불변(immutable)!
s = "Hello"
# s[0] = 'h'       # 에러! 직접 수정 불가
s = 'h' + s[1:]    # 새로 만들어야 함 → "hello"
```

### 인덱싱 & 슬라이싱
```python
s = "ABCDEF"
#    012345    (앞에서부터)
#   -6-5-4-3-2-1  (뒤에서부터)

# 인덱싱 (하나만)
s[0]      # 'A' (첫 글자)
s[3]      # 'D'
s[-1]     # 'F' (마지막)
s[-2]     # 'E' (뒤에서 두 번째)

# 슬라이싱 [시작:끝]  (끝은 미포함!)
s[0:3]    # 'ABC'   (인덱스 0, 1, 2)
s[2:5]    # 'CDE'   (인덱스 2, 3, 4)
s[:3]     # 'ABC'   (처음부터 3개)
s[3:]     # 'DEF'   (3부터 끝까지)
s[:]      # 'ABCDEF' (전체 복사)

# 슬라이싱 [시작:끝:간격]
s[::2]    # 'ACE'    (짝수 인덱스)
s[1::2]   # 'BDF'    (홀수 인덱스)
s[::-1]   # 'FEDCBA' (뒤집기! 매우 자주 사용)
```

### 문자열 연산
```python
# 연결
"Hello" + " " + "World"    # "Hello World"

# 반복
"Ha" * 3                    # "HaHaHa"
"-" * 20                    # "--------------------"

# 길이
len("Hello")                # 5

# 포함 확인
"llo" in "Hello"            # True
"xyz" in "Hello"            # False
```

---

## 2. 문자열 메서드 총정리

### 대소문자 변환
```python
s = "Hello World"
s.upper()        # "HELLO WORLD"    (전부 대문자)
s.lower()        # "hello world"    (전부 소문자)
s.swapcase()     # "hELLO wORLD"   (대↔소 반전)
s.capitalize()   # "Hello world"    (첫 글자만 대문자)
s.title()        # "Hello World"    (각 단어 첫 글자 대문자)
```

### 검색
```python
s = "Hello World Hello"

s.count('Hello')     # 2   (등장 횟수)
s.count('l')         # 4

s.find('World')      # 6   (처음 나오는 위치, 없으면 -1)
s.find('xyz')        # -1  (없으면 -1 → 에러 안남!)
s.rfind('Hello')     # 12  (뒤에서부터 찾기)

s.index('World')     # 6   (find와 같지만 없으면 에러!)

s.startswith('He')   # True  (이것으로 시작?)
s.endswith('lo')     # True  (이것으로 끝?)
```

### 판별 (True/False)
```python
"123".isdigit()      # True  (숫자로만?)
"abc".isalpha()      # True  (알파벳으로만?)
"abc123".isalnum()   # True  (알파벳 또는 숫자?)
"ABC".isupper()      # True  (전부 대문자?)
"abc".islower()      # True  (전부 소문자?)
"   ".isspace()      # True  (공백으로만?)
```

### 변환
```python
s = "Hello World"

s.replace('World', 'Python')   # "Hello Python"
s.replace('l', 'L')            # "HeLLo WorLd" (전부 교체)
s.replace('l', 'L', 1)         # "HeLlo World" (1개만 교체)
```

### 공백 제거
```python
s = "  Hello World  "
s.strip()       # "Hello World"    (양쪽 공백 제거)
s.lstrip()      # "Hello World  "  (왼쪽만)
s.rstrip()      # "  Hello World"  (오른쪽만)

# strip은 지정 문자도 제거 가능
"===Hello===".strip('=')   # "Hello"
```

---

## 3. split()과 join() (가장 중요!)

### split() : 문자열 → 리스트
```python
# 공백 기준 분리 (기본)
"Hello World Python".split()
# ['Hello', 'World', 'Python']

# 특정 문자 기준 분리
"1,2,3,4,5".split(',')
# ['1', '2', '3', '4', '5']

"2026-03-20".split('-')
# ['2026', '03', '20']

# 연속 공백 처리 차이
"  a  b  c  ".split()      # ['a', 'b', 'c']       (연속 공백 무시)
"  a  b  c  ".split(' ')   # ['', '', 'a', '', 'b', '', 'c', '', '']  (그대로)
# → 웬만하면 인자 없이 .split() 사용!

# 활용: 숫자 입력
a, b = map(int, input().split())
nums = list(map(int, input().split()))
```

### join() : 리스트 → 문자열
```python
# '구분자'.join(리스트)
' '.join(['Hello', 'World'])      # 'Hello World'
','.join(['a', 'b', 'c'])         # 'a,b,c'
''.join(['a', 'b', 'c'])          # 'abc' (구분자 없이 연결)
'\n'.join(['line1', 'line2'])     # 줄바꿈으로 연결

# 주의: join은 문자열 리스트만 가능!
# ','.join([1, 2, 3])             # 에러!
','.join(map(str, [1, 2, 3]))     # '1,2,3'  (str 변환 필요)
```

---

## 4. 아스키코드 (ord / chr)

```python
# ord(): 문자 → 숫자
ord('A')    # 65     대문자 A~Z: 65~90
ord('Z')    # 90
ord('a')    # 97     소문자 a~z: 97~122
ord('z')    # 122
ord('0')    # 48     숫자 0~9: 48~57
ord('9')    # 57

# chr(): 숫자 → 문자
chr(65)     # 'A'
chr(97)     # 'a'
chr(48)     # '0'

# 활용 1: 알파벳 전체 순회
for i in range(26):
    print(chr(ord('a') + i), end='')  # abcdefghijklmnopqrstuvwxyz

# 활용 2: 알파벳 몇 번째인지
ch = 'D'
pos = ord(ch) - ord('A')    # 3 (0부터 시작)

# 활용 3: 대소문자 변환 원리
ch = 'A'
lower_ch = chr(ord(ch) + 32)   # 'a' (대문자+32 = 소문자)

# 활용 4: 카이사르 암호 (문자 밀기)
ch = 'A'
shifted = chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))  # 'D'
```

---

## 5. 문자열 순회 패턴

```python
s = "Hello"

# 패턴 1: 문자 하나씩 순회
for ch in s:
    print(ch)        # H, e, l, l, o

# 패턴 2: 인덱스와 함께
for i in range(len(s)):
    print(i, s[i])   # 0 H, 1 e, 2 l, 3 l, 4 o

# 패턴 3: enumerate
for i, ch in enumerate(s):
    print(i, ch)

# 패턴 4: 문자 빈도수 세기
freq = [0] * 26   # 알파벳 26칸
for ch in s.lower():
    if ch.isalpha():
        freq[ord(ch) - ord('a')] += 1
# freq[7]=1(h), freq[4]=1(e), freq[11]=2(l), freq[14]=1(o)

# 패턴 5: 특정 문자 위치 모두 찾기
positions = [i for i, ch in enumerate(s) if ch == 'l']  # [2, 3]
```
