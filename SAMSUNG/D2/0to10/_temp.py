
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt ={}
    for char in str1:
        cnt[char]=0
    for char in str2:
        if char in cnt:
            cnt[char]+=1
    mx = 0
    for i in cnt.values():
        if i > mx:
            mx = i
    print(f'#{tc} {mx}')

