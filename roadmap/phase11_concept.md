# Phase 11. 최단경로 & 고급 그래프 - 개념

[< 로드맵 목차](../ROADMAP.md) | [문제 풀기 >](phase11_problems.md)

---

## 1. 다익스트라 (Dijkstra)

> 하나의 시작점에서 모든 노드까지의 최단 거리. **양의 가중치만** 가능.
> 시간복잡도: O(E log V) (힙 사용)

```python
import heapq

def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]   # (거리, 노드)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:   # 이미 더 짧은 경로 발견됨
            continue

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dist
```

---

## 2. 플로이드-워셜

> 모든 노드 쌍 간의 최단 거리. O(V³).

```python
INF = float('inf')
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

# 간선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

# 핵심: k를 거쳐가는 경우
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

---

## 3. 유니온-파인드 (Union-Find)

> 서로소 집합. "같은 그룹인지" 빠르게 판별.

```python
parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

# 사용
union(1, 2)
union(2, 3)
find(1) == find(3)   # True (같은 그룹)
```

---

## 4. 최소 신장 트리 (MST) - 크루스칼

> 모든 노드를 최소 비용으로 연결. 유니온-파인드 활용.

```python
edges.sort(key=lambda x: x[2])  # 비용순 정렬

total = 0
count = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost
        count += 1
        if count == n - 1:
            break
```
