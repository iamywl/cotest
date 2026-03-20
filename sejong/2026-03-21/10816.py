cnt_A = int(input())
inputs_A = list(map(int, input().split()))

cnt_B = int(input())
inputs_B = list(map(int, input().split()))

count = {}
for ele in inputs_A:
    count[ele] = count.get(ele, 0) + 1

print(" ".join(str(count.get(ele, 0)) for ele in inputs_B))
