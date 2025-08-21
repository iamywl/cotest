# src = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1&&&&&&&&&&

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    snail=[[0]*N for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y,m = 0,0,0
    for val in range(1, N*N+1):
        snail[x][y] = val
        next_x = x+dx[m]
        next_y = y+dy[m]
        if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N or snail[next_x][next_y] != 0:
            m = (m+1)%len(dx)
        x+= dx[m]
        y+= dy[m]
    print(f"#{testcase}")
    for row in snail:
        print(' '.join(map(str, row)))