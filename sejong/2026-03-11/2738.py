A, B = map(int, input().split())

matrix_A = []
matrix_B = []

for i in range(A):
    matrix_A.append(list(map(int, input().split())))
for i in range(A):
    matrix_B.append(list(map(int, input().split())))
for i in range(A):
    for j in range(B):
        matrix_A[i][j] += matrix_B[i][j]
for ele in matrix_A:
    print(" ".join(map(str, ele)))