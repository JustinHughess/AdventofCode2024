"""
def multiply_input(text):
    numbers = []
    start = 0
    while True:
        start_of_mul = text.find("mul(", start)
        if start_of_mul == -1:
            break

        end_of_mul = text.find(")", start_of_mul)
        if end_of_mul == -1:
            break

        inside = text[start_of_mul + 4:end_of_mul]
        parts = inside.split(',')
        if len(parts) == 2:
            x_str = parts[0].strip(" '\"")
            y_str = parts[1].strip(" '\"")
            try:
                x = int(x_str)
                y = int(y_str)
                numbers.extend([x, y])
            except ValueError:
                pass

        start = end_of_mul + 1

    total = 0
    for i in range(0, len(numbers), 2):
        total += numbers[i] * numbers[i + 1]

    return total


if __name__ == "__main__":
    with open("Day3Input.txt", "r") as file:
        full_input = file.read()

    print(multiply_input(full_input))
"""

import re

def multiply_input(text):
    total = 0
    pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    matches = re.findall(pattern, text)
    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        total += x * y
    return total

if __name__ == "__main__":
    with open("Day3Input.txt", "r") as file:
        full_input = file.read()

    print(multiply_input(full_input))