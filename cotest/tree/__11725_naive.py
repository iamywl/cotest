import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = [0] * (n + 1)
    front = 0
    rear = 0
    visited = [False] * (n + 1)

    queue[rear] = start
    # python은 rear++이런거 없음
    rear += 1
    visited[start] = True

    while front < rear:
        current = queue[front]
        front += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue[rear] = neighbor
                rear += 1

bfs(1)

for i in range(2, n + 1):
    print(parent[i])

