import time
from collections import deque

N = 100000  # 실험용 데이터 크기

# 리스트 실험
list_data = list(range(N))

start_time = time.time()
for _ in range(N):
    list_data.pop(0)  # 앞에서 제거 → 느림!
end_time = time.time()
print(f"list.pop(0) 실행 시간: {end_time - start_time:.5f}초")

# 덱 실험
deque_data = deque(range(N))

start_time = time.time()
for _ in range(N):
    deque_data.popleft()  # 앞에서 제거 → 빠름!
end_time = time.time()
print(f"deque.popleft() 실행 시간: {end_time - start_time:.5f}초")
