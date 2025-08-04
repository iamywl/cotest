N = int(input())
inputs = list(map(int , input().split()))
inputs.sort()
def find_midlle(arg):
    # index = int(round(len(arg)/2))
    index = len(arg) //2
    return arg[index]
print("test : ",find_midlle(inputs))

# def find_midlle(arg):
#     inputs = bubble_sort(arg)
#     return inputs[round(N)]

# def swap(arg1, arg2):
#     temp = arg1
#     arg1 = arg2
#     arg2 = temp
#     
# def bubble_sort(arg):
#     for i in range(len(arg)):
#         if arg[i] > arg[i+1]:
#             swap(arg[i], arg[i+1]) 

#print(round(4.5))