from pathlib import Path
from collections import Counter

root_directory = Path(__file__).parent
input_file = root_directory / 'Day1Input.txt'

left_array = []
right_array = []

with open('Day1Input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            left_array.append(int(parts[0]))
            right_array.append(int(parts[1]))

right_counts = Counter(right_array)

total = 0
for num in left_array:
    total += num * right_counts.get(num, 0)

print(total)

