#
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 설정

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

# 입력 처리
try:
    vertex = int(input("Input count(vertex) : "))  # 정점 수
    edge = int(input("Input count(edge) : "))      # 간선 수

    # 정점 수가 유효한 범위인지 확인 (문제 조건에 맞게)
    if vertex < 1 or vertex > 1000 or edge < 0 or edge > vertex * (vertex - 1) // 2:
        raise ValueError("Invalid input range.")

    # 그래프 초기화 list comprehension
    graph = [[] for _ in range(vertex + 1)]

    #graph = [] 
    #for i in range(vertex):
    #    graph.append([])

    visited = [False] * (vertex + 1)

    print("Input edges (u v) format:")

    for _ in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 연결 요소 개수 세기
    count = 0
    for i in range(1, vertex + 1):
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1

    print("Number of connected components:", count)

except ValueError as ve:
    print("입력 값이 유효하지 않습니다:", ve)
except Exception as e:
    print("오류가 발생했습니다:", e)
