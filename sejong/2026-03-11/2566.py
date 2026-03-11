# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

res_i = 0
res_j = 0
max = 0

inputs = []
for i in range(9):
    inputs.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if max < inputs[i][j]:
            max = inputs[i][j]
            res_i = i
            res_j = j
print(max)
print(f"{res_i+1} {res_j+1}")



