import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():
    try:
        n_str = input()
        if not n_str.strip(): return
        n = int(n_str)
    except (IOError, ValueError):
        return
    
    if n == 1:
        print(0)
        return

    graph = [[] for _ in range(n + 1)]

    for new_node in range(2, n + 1):
        u, w = map(int, input().split())
        graph[u].append((new_node, w))
        graph[new_node].append((u, w))

    def dfs(start_node):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        stack = [(start_node, 0)]
        
        farthest_node = start_node
        max_dist = 0

        while stack:
            curr_node, curr_dist = stack.pop()

            if curr_dist > max_dist:
                max_dist = curr_dist
                farthest_node = curr_node

            for neighbor, weight in graph[curr_node]:
                if distances[neighbor] == -1:
                    new_dist = curr_dist + weight
                    distances[neighbor] = new_dist
                    stack.append((neighbor, new_dist))
        
        return distances, farthest_node

    _, u = dfs(1)
    dist_from_u, v = dfs(u)
    dist_from_v, _ = dfs(v)

    radius = float('inf')
    for i in range(1, n + 1):
        eccentricity = max(dist_from_u[i], dist_from_v[i])
        if eccentricity < radius:
            radius = eccentricity
            
    print(radius)

while True:
    solve()