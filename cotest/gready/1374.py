# src = https://www.acmicpc.net/problem/1374

import sys
import heapq

def solve():
    N = int(sys.stdin.readline())
    lect = []
    for _ in range(N):
        _, start, end = map(int, sys.stdin.readline().split())
        lect.append((start, end))
    # 시작시간 기준 같으면 종료시작 기준
    lect.sort(key=lambda x: (x[0], x[1]))
    min_heap = [] 
    max_classrooms = 0
    for start_time, end_time in lect:
        #print(f"start_time = {start_time}, end_time = {end_time}")
        # 1.    (2,14)min_heap 비었음, min_heap [14], max_classrooms = 1
        # 2.    (3,8)min_heap Ture start_time(3) < min_heap[0] (14) 조건 건너뜀
        #           min_heap=[8,14] max_classrooms = (1,2) max_classrooms = 2 min_heap = [8,14], max_classrooms =2
        # 3.    (6,20)min_heap Ture start_time(6) < min_heap[0] (8) 조건 건너뒴
        #       heapq.heappush(min_heap, 20) -> min_heap = [8,14,20]
        #       max_classrooms = max(2,3),        min_heap = [8,14,20]
        # 4.    (6,27)min_heap Ture start_time(6) < min_heap[0] (8) 조건 건너뜀
        #        heapq.heappush(min_heap, 27) min_heap = [8,13,20,27]
        #        max_classrooms = max(3,4) max_classrooms = 4
        # 5.    (7,13)
        #       min_heap true start_time(7) < min_heap[0](8) 조건 건너쮬
        #       max_classrooms = max(4,5) max_classrooms = 5
        #       min_heap = [8,13,14,20,27], max_classrooms = 5
        # 5.    (12,18)
        #       min_heap start_time (12) > min_heap(8)
        #       heapq.heappop(min_heap) 8 제거 -> 최소값 제거 
        #       heapq.heappush(min_heap,18) min_heap = [13, 14, 18, 20, 27]

        #       기존의 강의실에 배정할 수 있는지 검증
        #       한강의실에서 2개이상의 강의 진행안됨, 한 강의가 종료되는 시간과 다른강의가 시작하는 시간이 겹치는 것은 허용된다.
        #       min_heap값이 비어있지 않으면 재활용 필요 없음.
        #       처리하는 시간(start_time)과 가장 빨리 비는 강의시간 min_heap[0]를 비교하여서가장 빨리 비는 강의실이 처리하는 강의시간보다 전이거나 동시인지 체크하면됨.
        
        
        if min_heap and start_time >= min_heap[0]:
            # c++ priority_queue
            heapq.heappop(min_heap)
        # push하면 알아서 소팅해줌
        heapq.heappush(min_heap, end_time)
        
        max_classrooms = max(max_classrooms, len(min_heap))

    print(max_classrooms)

solve()

