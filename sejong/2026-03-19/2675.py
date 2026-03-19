T = int(input())
res = []

for tc in range(1, T+1):
    n, inputs = input().split()
    for ele in inputs:
        res.append(ele*int(n) )
    print(f"".join(res))
    res = []