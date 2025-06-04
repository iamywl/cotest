import sys
input = sys.stdin.readline
n = int(input())
a = input().split()
A = []
for i in range(n):
    A.append(int(a[i]))

m = int(input())
b = input().split()
B = []
for i in range(m):
    B.append(int(b[i]))
def sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
def find(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == x:
            return 1
        elif arr[m] < x:
            s = m + 1
        else:
            e = m - 1
    return 0
sort(A)
for i in range(m):
    ok = find(A, B[i])
    print(ok, end=' ')
