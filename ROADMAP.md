# Python 코딩테스트 로드맵

> 각 Phase 폴더에서 **개념 학습 → 문제 풀기** 순서로 진행하세요.
>
> 이 파일은 **목차(인덱스)** 입니다. 상세 내용은 [`roadmap/`](roadmap/) 폴더의 개별 문서를 참고하세요.

```
roadmap/
├── phase01_concept.md     ← 개념 설명 (코드 예제 포함)
├── phase01_problems.md    ← BOJ 추천 문제 목록
├── phase02_concept.md
├── phase02_problems.md
├── ...
└── phase12_problems.md
```

---

## 로드맵 전체 구조

| Phase | 주제 | 난이도 | 링크 |
|:---:|------|:---:|:---:|
| 1 | Python 기초 & 입출력 | ★ | [개념](roadmap/phase01_concept.md) / [문제](roadmap/phase01_problems.md) |
| 2 | 문자열 처리 | ★ | [개념](roadmap/phase02_concept.md) / [문제](roadmap/phase02_problems.md) |
| 3 | 리스트 완전 정복 | ★~★★ | [개념](roadmap/phase03_concept.md) / [문제](roadmap/phase03_problems.md) |
| 4 | 딕셔너리 & 집합 & 튜플 | ★~★★ | [개념](roadmap/phase04_concept.md) / [문제](roadmap/phase04_problems.md) |
| 5 | 스택 & 큐 & 힙 | ★★ | [개념](roadmap/phase05_concept.md) / [문제](roadmap/phase05_problems.md) |
| 6 | 정렬 & 탐색 | ★★ | [개념](roadmap/phase06_concept.md) / [문제](roadmap/phase06_problems.md) |
| 7 | 수학 & 브루트포스 | ★~★★ | [개념](roadmap/phase07_concept.md) / [문제](roadmap/phase07_problems.md) |
| 8 | 그래프 탐색 (BFS/DFS) | ★★~★★★ | [개념](roadmap/phase08_concept.md) / [문제](roadmap/phase08_problems.md) |
| 9 | 동적 프로그래밍 (DP) | ★★~★★★ | [개념](roadmap/phase09_concept.md) / [문제](roadmap/phase09_problems.md) |
| 10 | 그리디 알고리즘 | ★★~★★★ | [개념](roadmap/phase10_concept.md) / [문제](roadmap/phase10_problems.md) |
| 11 | 최단경로 & 고급 그래프 | ★★★~★★★★ | [개념](roadmap/phase11_concept.md) / [문제](roadmap/phase11_problems.md) |
| 12 | 고급 주제 | ★★★★ | [개념](roadmap/phase12_concept.md) / [문제](roadmap/phase12_problems.md) |

> ★ 브론즈 / ★★ 실버 / ★★★ 골드 / ★★★★ 플래티넘

## 진행 상황

- [x] Phase 1 - 기초 입출력 (진행 중)
- [x] Phase 2 - 문자열 처리 (진행 중)
- [ ] Phase 3 - 리스트
- [ ] Phase 4 - 딕셔너리 & 집합
- [ ] Phase 5 - 스택 & 큐 & 힙
- [ ] Phase 6 - 정렬 & 탐색
- [ ] Phase 7 - 수학 & 브루트포스
- [ ] Phase 8 - BFS / DFS
- [ ] Phase 9 - DP
- [ ] Phase 10 - 그리디
- [ ] Phase 11 - 최단경로
- [ ] Phase 12 - 고급 주제

## 필수 라이브러리 요약

```python
import sys; input = sys.stdin.readline   # 빠른 입력
from collections import deque, defaultdict, Counter
import heapq
from itertools import permutations, combinations
import bisect
from functools import lru_cache
sys.setrecursionlimit(10**6)
```

## 시간복잡도 가이드

| N | 허용 복잡도 | | N | 허용 복잡도 |
|:---:|:---:|:---:|:---:|:---:|
| ≤ 10 | O(N!) | | ≤ 5,000 | O(N²) |
| ≤ 20 | O(2^N) | | ≤ 100,000 | O(N log N) |
| ≤ 500 | O(N³) | | ≤ 10,000,000 | O(N) |

## 자료구조 시간복잡도

| 연산 | list | dict/set | deque | heapq |
|:---:|:---:|:---:|:---:|:---:|
| 접근 [i] | O(1) | O(1) | O(n) | - |
| 검색 (in) | O(n) | **O(1)** | O(n) | O(n) |
| 끝 추가/삭제 | O(1) | O(1) | O(1) | O(log n) |
| 앞 추가/삭제 | O(n) | - | **O(1)** | - |
