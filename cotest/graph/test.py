import sys
sys.setrecursionlimit(10000)

def dfs(v, visited, graph):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

# 입력 받기
n, m = map(int, input().split())

#list comprehension
#graph = [[] for _ in range(n + 1)]

graph = [] 
for _ in range(n+1):
    graph.append([])
visited = [False] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, visited, graph)
        count += 1

print(count)
