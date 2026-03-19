T = int(input())


for tc in range(1, T+1):
    inputs = input()
    reversed_inputs = inputs[::-1]
    print(f'{inputs[0]}{reversed_inputs[0]}')
