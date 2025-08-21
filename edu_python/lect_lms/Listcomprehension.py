squares = []
for i in range(5):
    squares.append(i*i)
    print({i}, "squares", squares)

list_squares = [i*i for i in range(5)]
print("list comprehenion", {i}, "squares", list_squares)

