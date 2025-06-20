def is_safe(report):
    levels = list(map(int, report.split()))

    def check_safety(levels):
        is_increasing = True
        is_decreasing = True

        for i in range(len(levels) - 1):
            diff = abs(levels[i + 1] - levels[i])

            if diff < 1 or diff > 3:
                return False

            if levels[i] >= levels[i + 1]:
                is_increasing = False
            if levels[i] <= levels[i + 1]:
                is_decreasing = False

        return is_decreasing or is_increasing

    if check_safety(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if check_safety(modified_levels):
            return True
    return False

with open("Day2Input.txt", "r") as file:
    reports = file.readlines()

safe_count = 0
for report in reports:
    if is_safe(report.strip()):
        safe_count += 1

print(safe_count)
