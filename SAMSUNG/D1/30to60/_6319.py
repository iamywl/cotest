def reverse_string(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

word = input()

reversed_word = reverse_string(word)

if word == reversed_word:
    print(word)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(word)
    print("입력하신 단어는 회문이 아닙니다.")