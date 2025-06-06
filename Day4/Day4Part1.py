DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

def in_bounds(row, column, max_rows, max_columns):
    if row >= 0 and row < max_rows and column >= 0 and column < max_columns:
        return True
    else:
        return False

def find_xmas(grid, word):
    row_count = len(grid)
    col_count = len(grid[0])
    count = 0

    for r in range(row_count):
        for c in range(col_count):
            for direction in DIRECTIONS:
                dr = direction[0]
                dc = direction[1]

                match = True

                for k in range(len(word)):
                    new_row = r + dr * k
                    new_col = c + dc * k

                    if not in_bounds(new_row, new_col, row_count, col_count):
                        match = False
                        break

                    if grid[new_row][new_col] != word[k]:
                        match = False
                        break

                if match:
                    count += 1

    return count

def read_grid(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                row = list(stripped_line)
                grid.append(row)
    return grid

file = read_grid('Day4Input.txt')
word = "XMAS"
total = find_xmas(file, word)
print("Total XMAS Words Found:", total)