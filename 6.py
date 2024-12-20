from typing import Union, Tuple
input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
def main():
    input = open("6.input").read()
    grid, pos = get_positions(input)
    print("Part 1:",part1(grid, pos))
    print("Part 2:",part2(grid, pos))

def get_positions(grid: str) -> Union[list[list[str]], Tuple[int, int]]:
    grid = [list(row) for row in grid.strip().split('\n')]
    start_pos = [(x, y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == '^'][0]
    return grid, start_pos

def move(pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return (pos[0] + direction[0], pos[1] + direction[1])

def pretty_print_grid(grid: list[list[str]]) -> None:
    for x in range(len(grid)):
        print(''.join(grid[x]))

def is_safe(pos: Tuple[int, int], grid: list[list[str]]) -> bool:
    return pos[0] < len(grid) and pos[0] >= 0 and pos[1] < len(grid[0]) and pos[1] >= 0

def get_visited(grid: list[list[str]], pos: Tuple[int, int]) -> set[Tuple[int, int]]:
    visited = set()
    directions = [(-1,0),(0,1),(1, 0),(0, -1)]
    direction_index = 0
    while(is_safe(pos, grid)):
        visited.add(pos)
        new_pos = move(pos, directions[direction_index])
        if is_safe(new_pos, grid) and grid[new_pos[0]][new_pos[1]] == "#" :
            direction_index = (direction_index + 1) % 4
        else:
            pos = new_pos
    return visited

def part1(grid: list[list[str]], pos: Tuple[int, int]) -> int:
    return len(get_visited(grid, pos))

def can_complete(grid: list[list[str]], pos: Tuple[int, int]) -> bool:
    directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]
    direction_index = 0
    visited = set()
    if (grid[pos[0]][pos[1]] == "#"): return True
    while(is_safe(pos, grid)):
        if (pos, directions[direction_index]) in visited:
            return False
        visited.add((pos, directions[direction_index]))
        new_pos = move(pos, directions[direction_index])
        if is_safe(new_pos, grid) and grid[new_pos[0]][new_pos[1]] == "#" :
            direction_index = (direction_index + 1) % 4
        else:
            pos = new_pos
    return True

def part2(grid: list[list[str]], pos: Tuple[int, int]) -> int:
    blocked=0
    visited = get_visited(grid, pos)
    for obj_pos in visited:
            x, y = obj_pos
            grid[x][y] = "#"
            blocked+= not can_complete(grid, pos)
            grid[x][y] = "."
    return blocked

main()