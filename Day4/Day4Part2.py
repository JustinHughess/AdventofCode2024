def read_grid(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                row = list(stripped_line)
                grid.append(row)
    return grid

def is_valid_xmas(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])

    if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
        return False

    tl = grid[r - 1][c - 1]
    tr = grid[r - 1][c + 1]
    center = grid[r][c]
    bl = grid[r + 1][c - 1]
    br = grid[r + 1][c + 1]

    if center != 'A':
        return False

    diag1 = [tl, center, br]
    diag2 = [tr, center, bl]

    valid_diag = (
        diag1 == ['M', 'A', 'S'] or
        diag1 == ['S', 'A', 'M']
    )

    valid_other_diag = (
        diag2 == ['M', 'A', 'S'] or
        diag2 == ['S', 'A', 'M']
    )

    if valid_diag and valid_other_diag:
        return True

    return False

def count_xmas_x_shape(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_valid_xmas(grid, r, c):
                count += 1
    return count

grid = read_grid('Day4Input.txt')
total = count_xmas_x_shape(grid)
print("Total X-MAS Patterns Found:", total)