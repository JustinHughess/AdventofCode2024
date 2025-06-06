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