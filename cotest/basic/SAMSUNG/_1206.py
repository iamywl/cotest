TESTCASE_COUNT = 10

def solve():
    N = int(input())
    heights = list(map(int, input().split()))

    total_view_count = 0

    for j in range(2, N - 2):
        current_building_height = heights[j]

        if current_building_height == 0:
            continue

        surrounding_heights = [
            heights[j-2],
            heights[j-1],
            heights[j+1],
            heights[j+2]
        ]
        
        max_surrounding_height = max(surrounding_heights)

        if current_building_height > max_surrounding_height:
            view_secured_floors = current_building_height - max_surrounding_height
            total_view_count += view_secured_floors

    return total_view_count

for i in range(1, TESTCASE_COUNT + 1):
    result = solve()
  