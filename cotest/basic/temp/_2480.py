# src = https://www.acmicpc.net/problem/2480

boo0, boo1, boo2 = map(int, input().split())

def findlargest(a,b,c):
    temp = 0
    if a > temp:
        temp = a
    if b > temp:
        temp = b
    if c > temp:
        temp = c
    return temp


if (boo0 == boo1 and boo1 == boo2):
    print(10_000 + (boo0*1000))
# 2개가같을 경우
elif (boo0 == boo1) or (boo0 == boo2):
    print(1_000 + (boo0*100))
elif(boo1 == boo2):
        print(1_000 + boo1*100)
else:
    print(100 * findlargest(boo0,boo1,boo2))
