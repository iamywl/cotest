inputs = input()
res_alpha = '' 
upper_inputs = inputs.upper()

set_inputs= set(upper_inputs)
alpha_dict = {}
for ele in upper_inputs:
    if ele not in alpha_dict:
        alpha_dict[ele] = 0
    alpha_dict[ele] +=1
temp_max = max(alpha_dict.values())
vals = (alpha_dict.values())

#print(alpha_dict)
#print(temp_max)
coutner = 0

for kys, val in alpha_dict.items():
    if temp_max == val:
        coutner +=1
        res_alpha = kys
    
if coutner == 1:
    print(res_alpha)
else:
    print('?')