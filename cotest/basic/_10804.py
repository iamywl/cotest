# src = https://www.acmicpc.net/problem/10804
# target = [i for i in range(21)] # cards = [0, 1, 2, ..., 20]

target = []
for i in range(21):
    target(i)

for i in range(10):
    a, b = map(int, input().split())
    target[a,b+1] = target[a,b+1][::-1]
print(target)

# cards = [i for i in range(21)]
#
#for _ in range(10):
#    a, b = map(int, input().split())
#    cards[a : b+1] = cards[a : b+1][::-1]
#
#print(' '.join(map(str, cards[1:])))