# Phase 8. 그래프 탐색 (BFS/DFS) - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase08_problems.md)

---

## 1. 그래프란?

> 노드(정점)와 간선(연결)으로 이루어진 자료구조.
> SNS 친구 관계, 지도, 네트워크 등을 표현.

### 그래프 표현 방법

```python
# 인접 리스트 (가장 많이 사용!)
# 각 노드에 연결된 노드 목록을 저장
n, m = map(int, input().split())  # 노드 수, 간선 수
graph = [[] for _ in range(n + 1)]  # 1번 노드부터 사용

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)    # 양방향(무방향) 그래프

# 예: 1-2, 1-3, 2-4 연결
# graph[1] = [2, 3]
# graph[2] = [1, 4]
# graph[3] = [1]
# graph[4] = [2]

# 인접 행렬 (노드 수 적을 때)
graph = [[0] * (n+1) for _ in range(n+1)]
graph[a][b] = 1
graph[b][a] = 1   # 양방향
```

---

## 2. DFS (깊이 우선 탐색)

> 한 길로 끝까지 가본 뒤, 막히면 돌아와서 다른 길로.
> 스택 또는 재귀로 구현.

```python
# 재귀 DFS (가장 간결)
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    print(node, end=' ')       # 방문 처리

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)  # 1번 노드에서 시작

# 스택 DFS
def dfs_stack(start):
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
```

---

## 3. BFS (너비 우선 탐색)

> 가까운 곳부터 차례로 탐색. 큐(deque)로 구현.
> **최단 거리를 구할 때는 BFS!**

```python
from collections import deque

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

bfs(1)
```

### BFS로 최단 거리 구하기
```python
from collections import deque

def bfs_dist(start):
    dist = [-1] * (n + 1)    # -1: 미방문
    dist[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                queue.append(next_node)

    return dist
```

---

## 4. 2차원 격자 BFS/DFS (미로 탐색)

> 상하좌우 이동하는 문제. dx, dy 패턴이 핵심!

```python
from collections import deque

# 상하좌우 방향 벡터
dx = [-1, 1, 0, 0]   # 행: 위, 아래
dy = [0, 0, -1, 1]   # 열: 왼, 오

def bfs_grid(sx, sy):
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):   # 4방향
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위 체크 + 방문 체크 + 벽 체크
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist
```

### 연결 요소 개수 세기
```python
# 그래프에서 연결된 덩어리가 몇 개인지
count = 0
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)         # 또는 bfs(i)
        count += 1     # 새로운 덩어리 발견!

print(count)
```

---

## DFS vs BFS 언제 쓸까?

| | DFS | BFS |
|:---:|:---:|:---:|
| 구현 | 재귀/스택 | 큐(deque) |
| 특징 | 깊이 우선 | 너비 우선 |
| **최단거리** | X | **O** |
| 연결요소 | O | O |
| 모든 경로 | O | X |
| 메모리 | 적음 | 많음 |
