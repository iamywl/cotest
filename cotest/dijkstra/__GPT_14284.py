# src = https://www.acmicpc.net/problem/14284

import sys

# DSU (Disjoint Set Union) 자료구조:
#   정점 연결 상태를 효율적으로 관리.
#   각 정점이 속한 집합의 대표 원소를 찾아 그룹을 식별하고, 두 그룹을 합친다.
parent = [] # 각 정점의 부모 저장. (예: parent[i]는 i의 부모 정점)
sizes = []  # 각 집합의 크기 저장. (합칠 때 작은 집합을 큰 집합에 붙여 효율 증대)

def find(x):
    # 루트 노드(집합의 대표) 찾기:
    #   현재 정점 x가 자기 자신을 부모로 가리키면 루트.
    if parent[x] == x:
        return x
    # 경로 압축:
    #   루트가 아니면, 부모를 따라가면서 동시에 현재 정점의 부모를 바로 루트로 연결.
    #   다음 탐색 시 시간 단축.
    parent[x] = find(parent[x]) 
    return parent[x]

def union(x, y):
    # 두 정점 x, y의 대표 찾기:
    root_x = find(x)
    root_y = find(y)

    # 두 집합 합치기:
    #   대표가 다르면 두 정점은 다른 집합에 속해 있으므로 합쳐야 한다.
    if root_x != root_y:
        # 크기 기반 합치기:
        #   항상 작은 집합을 큰 집합의 자식으로 만들어 트리의 높이를 낮게 유지.
        if sizes[root_x] < sizes[root_y]:
            parent[root_x] = root_y
            sizes[root_y] += sizes[root_x]
        else:
            parent[root_y] = root_x
            sizes[root_x] += sizes[root_y]
        return True # 합병 성공
    return False # 이미 같은 집합이었음

def solve():
    # 1. 입력 데이터 로드:
    #   N: 정점 개수 (2 <= N <= 5000)
    #   M: 간선 리스트의 간선 수 (1 <= M <= 100,000)
    N, M = map(int, sys.stdin.readline().split())

    edges = [] # 간선 목록: (가중치, 정점1, 정점2) 튜플 저장
    for _ in range(M):
        u, v, c = map(int, sys.stdin.readline().split())
        edges.append((c, u, v)) # 가중치를 첫 요소로 둬 정렬에 유리

    #   S_node, T_node: 연결 여부를 확인할 두 특정 정점
    S_node, T_node = map(int, sys.stdin.readline().split())

    # 2. 간선 정렬:
    #   문제 목표: s와 t 연결 시점까지의 '최소 가중치 합'.
    #   전략: 가중치가 가장 낮은 간선들부터 그래프에 추가해야 최적. (크루스칼 유사)
    #   코드: edges 리스트를 튜플의 첫 번째 요소(가중치) 기준 오름차순 정렬.
    edges.sort()

    # 3. DSU 초기화:
    #   문제: 각 정점이 처음에는 독립적인 집합. 그룹들을 효율적으로 관리해야 한다.
    #   전략: DSU를 사용해 각 정점을 자신만의 집합으로 초기화.
    #   코드: parent[i]=i, sizes[i]=1 (정점 번호 1~N이므로 N+1 크기 배열)
    global parent, sizes # 함수 내 전역 변수 접근 허용
    parent = [i for i in range(N + 1)] 
    sizes = [1] * (N + 1)

    # 4. 간선 순차적 추가 및 연결 확인:
    #   문제: 정렬된 간선을 하나씩 추가하며, s와 t가 연결되는 최초 시점을 찾아야 한다.
    #   목표: 그 시점까지 추가된 '모든 간선'의 가중치 합이 최종 답.
    current_total_weight = 0 # s와 t가 연결될 때까지 추가된 간선들의 총 가중치

    #   정렬된 edges에서 (가중치, 정점1, 정점2)를 순서대로 가져온다.
    for weight, u, v in edges:
        #   간선 추가 조건:
        #     u와 v가 현재 다른 집합에 속해 있을 때만 (사이클 형성 방지).
        #     union 함수가 True를 반환하면 성공적으로 합쳐진 것.
        if union(u, v):
            #   간선 가중치 누적:
            #     새롭게 연결된 간선의 가중치를 총 합에 더한다.
            current_total_weight += weight
            
            #   s와 t 연결 여부 확인:
            #     s_node와 T_node가 같은 집합에 속하는지 확인. (find로 루트 비교)
            if find(S_node) == find(T_node):
                #   최종 결과 출력 및 종료:
                #     s와 t가 연결된 최초 시점이므로, 이때까지의 총 가중치 합이 최소.
                print(current_total_weight)
                return # 함수 즉시 종료

# 프로그램 실행 진입점:
#   스크립트가 직접 실행될 때 solve() 함수 호출.
if __name__ == "__main__":
    solve()