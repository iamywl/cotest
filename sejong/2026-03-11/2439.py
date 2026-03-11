N = int(input())
res = []

star = '*'
void = ' '
for i in range(N-1,-1,-1):
    j = N-i
    #print(f"i: {i} j :{j}")
    res.append(void*i)
    res.append(star*j)
    print(f"{''.join(map(str, res))}")
    res = []

# star void 
#  4     1 
#  3     2 
#  2     3  
#  1     3 
