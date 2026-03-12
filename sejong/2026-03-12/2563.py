T = int(input())
matrix = [[0 for col in range(100)] for row in range(100)]

inputs_x = []
inputs_y = []

for tc in range(1, T+1):
    x , y= map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1
            #print(f"{i} {j}")

res = 0 
for row in matrix:
    res += sum(row)

print(res)
#print(matrix)