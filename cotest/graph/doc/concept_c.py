import sys
sys.setrecursionlimit(10000)

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

try:
    vertex, edge = map(int, input().split())  # 순서 주의: vertex, edge

    if vertex < 1 or vertex > 1000 or edge < 0 or edge > vertex * (vertex - 1) // 2:
        raise ValueError("Invalid input range.")

    graph = []
    i = 0
    while i <= vertex:
        graph.append([])
        i += 1

    visited = []
    i = 0
    while i <= vertex:
        visited.append(False)
        i += 1

    i = 0
    while i < edge:
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        i += 1

    count = 0
    i = 1
    while i <= vertex:
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1
        i += 1

    print(count)

except ValueError as ve:
    print("입력 값이 유효하지 않습니다:", ve)
except Exception as e:
    print("오류가 발생했습니다:", e)
