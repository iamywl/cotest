#
# var = input("Type : Hello World",)
# int1 = int(input("Type : intger World",))
# int2 = input("Type : intger World",)
#
# print(var)
# print(int1 + 1)
# print(int2 + 1)

# var_map1, var_map2 = map(int , input("Type : var map : ",).split())
# print(var_map1, var_map2)
#



T = int(input())
prefix_sum = 0

for i in range(1,T+1):
    numbers =list(map(int, input().split()))
    
for i in range(0, len(numbers)):
	if not (numbers[i] % 2 == 0):
		prefix_sum = prefix_sum + numbers[i]

for i in range(1,T+1):
	print(f"#{i} , {prefix_sum}")