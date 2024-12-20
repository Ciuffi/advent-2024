from typing import Union

input = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""
input = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
def main():
    input = open("4.input").read()
    input = sanatize_input(input)
    print("Part 1:",part1(input))
    print("Part 2:",part2(input))

def sanatize_input(input: str) -> list[list[str]]:
    input = input.strip().splitlines()
    return [list(i) for i in input]

def part1(input: list[list[str]]) -> int:
    lines = [''.join(row) for row in input]
    lines.extend([''.join([row[i] for row in input]) for i in range(len(input))])
    bottom_left_diag, bottom_right_diag = collect_diagonals(input)
    lines.extend(bottom_left_diag)
    lines.extend(bottom_right_diag)
    return sum([line.count("XMAS") + line.count("SAMX") for line in lines])

def count_x_mas(input: list[list[str]], x: int, y: int) -> int:
    if not (x+1 < len(input) and x-1 >= 0) or not (y+1 < len(input[x]) and y-1 >= 0):
        return 0
    left_diag: str = "".join(input[x + dx][y + dy] for dx, dy in [(-1, -1), (0, 0), (1, 1)])
    right_diag: str = "".join(input[x + dx][y + dy] for dx, dy in [(-1, 1), (0, 0), (1, -1)])
    if(left_diag.count("SAM") + left_diag.count("MAS") and right_diag.count("MAS") + right_diag.count("SAM")):
        return 1
    return 0

def part2(input: list[list[str]]) -> int:
    total = 0
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == "A":
                total += count_x_mas(input, x, y)
    return total


def collect_diagonals(matrix: list[list[str]]) -> Union[list[str], list[str]]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    # For bottom-left diagonals
    bottom_left = []
    for start_col in range(cols):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        bottom_left.append(''.join(diagonal))
    
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, cols - 1
        while row < rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        bottom_left.append(''.join(diagonal))
    
    # For bottom-right diagonals
    bottom_right = []
    for start_col in range(cols):
        diagonal = []
        row, col = 0, start_col
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        bottom_right.append(''.join(diagonal))
    
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, 0
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        bottom_right.append(''.join(diagonal))
    
    return bottom_left, bottom_right
main()