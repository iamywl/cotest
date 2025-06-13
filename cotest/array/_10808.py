# src = https://www.acmicpc.net/problem/10808
#a b c d e f g h i j k l m n o p q r s t u v w x y z
import sys
from collections import defaultdict
S = sys.stdin.readline().strip()
char_counts = defaultdict(int) 
for char in S:
    char_counts[char] += 1
result = []
for i in range(ord('a'), ord('z') + 1):
    char = chr(i) 
    result.append(str(char_counts[char])) 
print(' '.join(result))