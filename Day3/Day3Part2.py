import re

file_path = "Day3Input.txt"

with open(file_path, "r") as f:
    file = f.read()

summa = 0

pattern = re.compile(r"don't\(\)\s*do\(\)(.*?)(?=don't\(\)|\Z)", re.DOTALL)
blocks = pattern.findall(file)

for block in blocks:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", block)
    for x, y in matches:
        summa += int(x) * int(y)

print(summa)
