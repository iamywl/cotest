#src = https://www.acmicpc.net/problem/1919
from collections import Counter

def solve():
    word1 = input()
    word2 = input()

    # 각 단어의 문자 빈도수 계산
    count1 = Counter(word1)
    count2 = Counter(word2)

    removed_chars = 0

    # 모든 알파벳에 대해 비교
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        
        # 두 단어에서 해당 문자의 개수 가져오기
        count_in_word1 = count1[char]
        count_in_word2 = count2[char]
        
        # 두 개수의 차이만큼이 제거해야 할 문자 수
        removed_chars += abs(count_in_word1 - count_in_word2)
            
    print(removed_chars)

solve()