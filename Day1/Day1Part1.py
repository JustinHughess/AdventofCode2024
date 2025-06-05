from pathlib import Path

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

left_array.sort()
right_array.sort()

difference = 0

for i in range(len(left_array)):
    if left_array[i] > right_array[i]:
        difference += left_array[i] - right_array[i]
    else:
        difference += right_array[i] - left_array[i]

print(difference)




