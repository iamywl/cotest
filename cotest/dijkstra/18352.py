# src = https://www.acmicpc.net/submit/18352

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

# 그래프 정보를 저장할 리스트를 반복문으로 생성
graph = []
for _ in range(n + 1):
    graph.append([])

#graph = [
    # []
    # []
    # []
    # []
    # []
    # []
# ]
# graph edge로 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 정보를 저장할 리스트를 -1로 초기화
# 문제에서 -1로 해달라고함.(없는 경우)
distance = [-1] * (n + 1)
queue = deque()
distance[x] = 0
queue.append(x)

while queue:
    now = queue.popleft()
    # graph[1] 2,3 부터 탐색시작
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

answer = []
for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for city in answer:
        print(city)