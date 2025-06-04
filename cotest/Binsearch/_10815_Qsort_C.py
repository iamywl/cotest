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

def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = arr[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= right and arr[i] <= pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i > j:
            # tuple unpacking........./??????
            # tmp = arr[left]
            # arr[left] = arr[j]
            # arr[j] = tmp
            arr[left], arr[j] = arr[j], arr[left]
        else:
            arr[i], arr[j] = arr[j], arr[i]
    quicksort(arr, left, j - 1)
    quicksort(arr, j + 1, right)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

quicksort(A, 0, n - 1)

ans =[]
for i in range(m):
    found = binary_search(A, B[i])
    ans.append(found)
    print(f"{found}")

print(f"ans : {ans}")