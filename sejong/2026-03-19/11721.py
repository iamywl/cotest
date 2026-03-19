inputs = input()
cnt =0
res = []
for idx in range(len(inputs)):
    cnt +=1
    res.append(inputs[idx])
    if idx == len(inputs):
        print(res)
    elif cnt == 10 or idx == len(inputs)-1:
        print(f"".join(res))
        res = []
        cnt = 0
