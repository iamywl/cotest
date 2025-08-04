#src = https://www.acmicpc.net/problem/1919
import sys 
input = sys.stdin.readline

def solve_without_counter():
    word1 = input()
    word2 = input()

    count1 = [0] * 26
    count2 = [0] * 26

    for char in word1:
        index = ord(char) - ord('a')
        count1[index] += 1

    for char in word2:
        index = ord(char) - ord('a')
        count2[index] += 1

    removed_chars = 0
    for i in range(26):
        removed_chars += abs(count1[i] - count2[i])
            
    print(removed_chars)

solve_without_counter()