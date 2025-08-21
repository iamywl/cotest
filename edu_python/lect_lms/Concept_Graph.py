n = 5
edges = [(0,1),(0,4),(1,2),(1,4),(2,3)]

#init list
adj_list = [[] for _ in range(5)]

print("adj_list : ", adj_list)


for i, (u, v) in enumerate(edges, start=0):
    adj_list[u].append(v)
    adj_list[v].append(u)
    print(f"{i}: {u}-{v}")
