N, X = map(int, input().split())

A = list(map(int,input().split()))
res = []

for ele in A:
    if ele < X:
        res.append(ele)
    
print(" ".join(map(str, res)))