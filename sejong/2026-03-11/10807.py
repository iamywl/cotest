N = int(input())

inputs = list(map(int, input().split()))
val = int(input())
cnt = 0

for ele in inputs:
    if ele == val:
        cnt +=1

print(cnt)