# src = https://www.acmicpc.net/problem/10809

# 아스키 값을 구하자..

 #inputs = input().split()
 #res = [-1]*26
 #arg = []
 #for i in range(26):
 #    char_to_find = chr(ord('a') + i)
 #    pos = inputs.find(char_to_find)
 #    res[i]= pos
 #
 #print(' '.join(map(str, res)))

inputs = input()
res = [-1] * 26
for i in range(26):
    finder = chr(ord('a')+i)
    pos = inputs.find(finder)
    res[i] = pos
print(' '.join(map(str, res)))