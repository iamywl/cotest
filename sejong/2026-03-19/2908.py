A, B = map(str, input().split())

reversed_A = A[::-1]
reversed_B = B[::-1]



if int(reversed_A) > int(reversed_B):
    print(reversed_A)
if int(reversed_A) <= int(reversed_B):
    print(reversed_B)
    