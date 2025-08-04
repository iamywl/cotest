# 테스트 케이스의 개수 T를 입력받습니다.
T = int(input())
# inputs = list(map(int, input()))
for testnum in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # for _ in range(N):
    #     snail.append([0]*N)
        
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    for num in range(1, N * N + 1):
        snail[x][y] = num
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            d = (d + 1) % 4
        x += dx[d]
        y += dy[d]

    print(f"#{testnum}")
    for row in snail:
        print(' '.join(map(str, row)))