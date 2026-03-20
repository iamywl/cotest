# Phase 4. 딕셔너리 & 집합 & 튜플 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase04_problems.md)

---

## 1. 딕셔너리 (dict)

> 키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료구조.
> 리스트는 인덱스(0,1,2...)로 접근하지만, 딕셔너리는 **키로 접근**.

### 기본 사용법
```python
# 생성
d = {}                              # 빈 딕셔너리
d = dict()                          # 같은 의미
d = {'apple': 3, 'banana': 5}       # 초기값

# 추가 & 수정
d['cherry'] = 7                     # 새 키 추가
d['apple'] = 10                     # 기존 키 수정 (덮어씀)

# 접근
d['apple']                          # 10 (없는 키면 KeyError!)
d.get('apple')                      # 10
d.get('melon', 0)                   # 0 (없으면 기본값 반환, 에러 안남!)

# 삭제
del d['banana']                     # 키로 삭제
val = d.pop('cherry')               # 삭제 + 값 반환 (7)
val = d.pop('xyz', -1)              # 없으면 기본값 반환 (-1)
```

### 딕셔너리 순회
```python
d = {'apple': 3, 'banana': 5, 'cherry': 7}

# 키 순회 (가장 기본)
for key in d:
    print(key, d[key])
# apple 3
# banana 5
# cherry 7

# 키-값 동시 순회 (가장 편리!)
for key, value in d.items():
    print(key, value)

# 키만, 값만
for key in d.keys():     print(key)
for val in d.values():   print(val)

# 포함 확인
'apple' in d          # True  (키가 있는지)
'melon' not in d      # True
3 in d.values()       # True  (값이 있는지, 느림)

# 길이
len(d)                # 3 (키의 개수)
```

### 실전 패턴 1: 빈도수 세기 (가장 자주 쓰임!)
```python
# 방법 1: 기본 if문
text = "hello world"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 방법 2: get 활용 (더 깔끔!)
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
# get(ch, 0): ch가 있으면 그 값, 없으면 0 반환

# 방법 3: Counter (가장 간단!)
from collections import Counter
freq = Counter(text)
freq.most_common(3)    # [('l', 3), ('o', 2), ('h', 1)]  상위 3개
freq['l']              # 3
freq['z']              # 0 (없는 키도 에러 안남!)
```

### 실전 패턴 2: 매핑 테이블
```python
# 값을 다른 값으로 변환할 때
grade_point = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0}
score = grade_point['A']   # 4.0

# 다이얼 문제 같은 매핑
dial = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6,
        'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}

# 또는 각 글자마다 직접 매핑
char_to_num = {}
for letters, num in dial.items():
    for ch in letters:
        char_to_num[ch] = num
# {'A': 3, 'B': 3, 'C': 3, 'D': 4, ...}
```

### 실전 패턴 3: 양방향 매핑
```python
# 이름 ↔ 번호 양방향 검색
name_to_id = {}
id_to_name = {}

n = int(input())
for i in range(1, n + 1):
    name = input().strip()
    name_to_id[name] = i
    id_to_name[i] = name

# 검색
query = input().strip()
if query.isdigit():
    print(id_to_name[int(query)])   # 번호 → 이름
else:
    print(name_to_id[query])        # 이름 → 번호
```

### 실전 패턴 4: defaultdict
```python
from collections import defaultdict

# 기본값이 자동으로 설정되는 딕셔너리
# 일반 dict: 없는 키 접근 → KeyError
# defaultdict: 없는 키 접근 → 기본값 자동 생성

# int → 기본값 0
counter = defaultdict(int)
for ch in "hello":
    counter[ch] += 1       # 없는 키도 에러 없이 0+1

# list → 기본값 []
groups = defaultdict(list)
students = [('A', '김'), ('B', '이'), ('A', '박')]
for cls, name in students:
    groups[cls].append(name)
# {'A': ['김', '박'], 'B': ['이']}

# set → 기본값 set()
graph = defaultdict(set)
```

---

## 2. 집합 (set)

> 중복 없이, 순서 없이 데이터를 저장. 검색이 O(1)로 매우 빠름!

### 기본 사용법
```python
# 생성
s = set()                       # 빈 집합 ({} 는 딕셔너리!)
s = {1, 2, 3, 4, 5}
s = set([1, 2, 2, 3, 3, 3])    # {1, 2, 3} 자동 중복 제거!

# 추가 & 삭제
s.add(6)                        # 추가
s.remove(3)                     # 삭제 (없으면 KeyError!)
s.discard(3)                    # 삭제 (없어도 에러 안남)
s.pop()                         # 아무거나 하나 제거

# 포함 확인 (핵심! O(1)!)
3 in s                          # True/False
```

### 집합 연산 (매우 유용!)
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합 (둘 중 하나라도)
a | b                   # {1, 2, 3, 4, 5, 6}
a.union(b)              # 같은 결과

# 교집합 (둘 다 있는)
a & b                   # {3, 4}
a.intersection(b)       # 같은 결과

# 차집합 (a에만 있는)
a - b                   # {1, 2}
a.difference(b)         # 같은 결과

# 대칭 차집합 (하나에만 있는)
a ^ b                   # {1, 2, 5, 6}
a.symmetric_difference(b)

# 부분집합
{1, 2}.issubset({1, 2, 3})        # True
{1, 2, 3}.issuperset({1, 2})      # True
```

### set의 핵심: 빠른 검색!
```python
# 리스트에서 검색: O(n) → 느림!
big_list = list(range(1000000))
999999 in big_list          # 매우 느림

# set에서 검색: O(1) → 빠름!
big_set = set(range(1000000))
999999 in big_set           # 즉시

# 실전: 존재 여부를 여러 번 확인해야 할 때
n = int(input())
cards = set(map(int, input().split()))   # set으로 변환!
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(1 if t in cards else 0)   # O(1)로 확인
```

### 중복 제거
```python
# 리스트 중복 제거
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))       # [1, 2, 3, 4] (순서 보장 안됨!)

# 순서 유지하면서 중복 제거
seen = set()
unique = []
for x in nums:
    if x not in seen:
        seen.add(x)
        unique.append(x)
# [1, 2, 3, 4] (순서 유지)
```

---

## 3. 튜플 (tuple)

> 리스트와 비슷하지만 **수정 불가(immutable)**. 딕셔너리 키로 사용 가능.

```python
# 생성
t = (1, 2, 3)
t = 1, 2, 3           # 괄호 생략 가능
t = (1,)               # 원소 하나일 때 쉼표 필수!
t = tuple([1, 2, 3])   # 리스트 → 튜플

# 접근 (리스트와 동일)
t[0]      # 1
t[-1]     # 3
t[1:3]    # (2, 3)

# 수정 불가!
# t[0] = 10  # TypeError!

# 언패킹 (값 분리)
a, b, c = (1, 2, 3)    # a=1, b=2, c=3
a, b = b, a             # 값 교환! (swap)
```

### 튜플을 쓰는 이유
```python
# 1. 여러 값 리턴
def min_max(nums):
    return min(nums), max(nums)     # 튜플로 리턴
lo, hi = min_max([3, 1, 4])        # 언패킹

# 2. 딕셔너리 키 (리스트는 키 불가!)
visited = {}
visited[(1, 2)] = True    # 좌표를 키로 (BFS에서 자주 사용)
# visited[[1, 2]] = True  # 에러! 리스트는 키 불가

# 3. 정렬 시 다중 기준
students = [('김', 90), ('이', 85), ('박', 90)]
students.sort(key=lambda x: (-x[1], x[0]))
# 점수 내림차순, 같으면 이름 오름차순
# [('김', 90), ('박', 90), ('이', 85)]
```
