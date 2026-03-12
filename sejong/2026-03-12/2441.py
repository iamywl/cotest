
star = '*'
void = ' '

N = int(input())

for i in range(N,0,-1):
    print(f"{void*(N-i)}{star*i}")
    #print(f"i{i} j{N-i-1}")