import sys
from collections import deque

def sol():
    # 입력 처리
    N, M = map(int, sys.stdin.readline().split())

    # for _ in range(1, N+1):까지 순회하면서 인접리스트 생성
    adj = [[] for _ in range(N + 1)]
   # 양방향이라서  A -> B b->A도 해줘얗.ㅁ 
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    #방문 체크
    visi = [0] * (N + 1) # Renamed to visi
    ans = 1
    MOD = 1_000_000_007
    # 모든 경우 전부다 순회해야해서 방문안했으면  큐에 집어넣고 방문하기
    for i in range(1, N + 1):
        if visi[i] == 0: # Check visi
            q = deque([i])
            visi[i] = 1 # Mark visi
            nodes_in_component = 0
            # 큐가 비어있지 않는 동안 계속 탐색함. 
            while q:
                u = q.popleft()
                # 모든 튜터 튜티에게 전달되어야해서
                # nodes_in_component를 선언해두고 찾고있는 트리의 교육생수를 누계저장
                nodes_in_component += 1
                for v in adj[u]:
                    if visi[v] == 0:
                        visi[v] = 1 
                        q.append(v)
            ans = (ans * nodes_in_component) % MOD
    print(ans)
sol()