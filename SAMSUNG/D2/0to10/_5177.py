# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTtiyIqd_wDFAVT&categoryId=AWTtiyIqd_wDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=2
def enq(item):
    global last
    # 1. 힙의 마지막 위치에 새 노드 추가
    last += 1
    heap[last] = item
    c = last
    p = c // 2
    while p >= 1 and heap[p] > heap[c]:
        #swap(heap[p], heap[c])
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0
    for x in arr:
        enq(x)
    ans = 0
    parent_idx = N // 2
    while parent_idx >= 1:
        ans += heap[parent_idx]
        parent_idx //= 2
    
    print(f"#{test_case} {ans}")
