T = int(input())
for i in range(1,T+1):
    numbers =list(map(int, input().split()))
    prefix_sum = 0
    for j in range(0, len(numbers)):
        # print("numbers:" , numbers[j])
        if numbers[j] % 2 == 1:
            prefix_sum = prefix_sum + numbers[j]
    print(f"#{i} , {prefix_sum}")

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    print(f"#{test_case} {total}")
