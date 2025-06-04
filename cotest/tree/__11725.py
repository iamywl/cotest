import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)  # 부모를 저장할 배열

# 2. 간선 정보로 트리 구성
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 3. BFS로 탐색하며 부모 설정
def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for neighbor in graph[now]:
            if not visited[neighbor]:
                parent[neighbor] = now
                visited[neighbor] = True
                queue.append(neighbor)

bfs(1)

# 4. 결과 출력 (2번 노드부터)
for i in range(2, n + 1):
    print(parent[i])

