# src = https://www.acmicpc.net/problem/3724

def solve():
    M, N = map(int, input().split())
    col_prod = [1] * M 

    for n_idx in range(N):
        row_vals = list(map(int, input().split()))
        
        for m_idx in range(M):
            col_prod[m_idx] *= row_vals[m_idx]
   ## 파이썬은 타입 실수범위 이런거 안따짐. 그래서 무한대라는 상태를 따로 정의해줘서 맥스 구현... 
   # 최대 값이 음수일 수도 있어서 음수의 최대값장 저장
    max_val = -float('inf')
    res_col_idx = -1     
    # find max
    # 맥스로 한번에 찾을 수 있는데, idx의 최대를 찾아야해서 편한대로 구현..
    for m_idx in range(M):
        curr_prod = col_prod[m_idx]
        
        if curr_prod > max_val:
            max_val = curr_prod
            res_col_idx = m_idx
        elif curr_prod == max_val:
            if m_idx > res_col_idx:
                res_col_idx = m_idx

    print(res_col_idx + 1)

# Test 케이스 개수 받기
T = int(input())

#T번만큼 sol호출
for t_idx in range(T):
    solve()