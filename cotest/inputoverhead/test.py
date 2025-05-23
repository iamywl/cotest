import sys
import time
import csv

input = sys.stdin.readline

def generate_input_file(filename, line_count):
    with open(filename, "w") as f:
        for i in range(line_count):
            f.write(f"{i}\n")

def measure_time_with_input(filename, line_count):
    start = time.time()
    original_stdin = sys.stdin
    with open(filename, "r") as f:
        sys.stdin = f
        for _ in range(line_count):
            _ = input()
    sys.stdin = original_stdin
    end = time.time()
    return end - start

def measure_time_with_sys_readline(filename, line_count):
    start = time.time()
    with open(filename, "r") as f:
        for _ in range(line_count):
            _ = f.readline()
    end = time.time()
    return end - start

# 테스트할 줄 수 리스트
test_cases = [10_000, 100_000, 1_000_000, 10_000_000]

# 결과 저장
results = []

for lines in test_cases:
    input_file = f"test_input_{lines}.txt"
    generate_input_file(input_file, lines)

    print(f"테스트 시작: {lines}줄")
    time_input = measure_time_with_input(input_file, lines)
    time_sys_readline = measure_time_with_sys_readline(input_file, lines)
    ratio = round(time_input / time_sys_readline, 2) if time_sys_readline > 0 else float('inf')

    results.append([lines, round(time_input, 4), round(time_sys_readline, 4), ratio])

# CSV 저장
with open("test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["줄 수", "input() 시간", "sys.stdin.readline() 시간", "차이 비율"])
    writer.writerows(results)

print("✅ 테스트 완료! 결과는 test.csv에 저장되었습니다.")
