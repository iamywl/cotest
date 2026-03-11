N, M = map(int,input().split())

list_inputs = []
if N ==1 and M ==1:
    print(1)
else:
    for ele in range(M):
        for i in range(ele):
            list_inputs.append(int(ele))
    print(sum(list_inputs[N-1:M]))
#print((list_inputs[N-1:M]))