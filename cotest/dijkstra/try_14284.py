# src = https://www.acmicpc.net/problem/14284
import sys

parent = []
sizes = []

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if sizes[a] < sizes[b]:
            a, b = b, a
        parent[b] = a
        sizes[a] += sizes[b]
        return True
    return False

def sol():
    N, M = map(int, sys.stdin.readline().split())

    edges = []
    for _ in range(M):
        u, v, c = map(int, sys.stdin.readline().split())
        edges.append((c, u, v))

    s_node, t_node = map(int, sys.stdin.readline().split())

    edges.sort()

    global parent, sizes
    parent = [i for i in range(N + 1)]
    sizes = [1] * (N + 1)

    total_cost_so_far = 0

    for weight, u, v in edges:
        if union_sets(u, v):
            total_cost_so_far += weight
            
            if find_set(s_node) == find_set(t_node):
                print(total_cost_so_far)
                return

if __name__ == "__main__":
    sol()
