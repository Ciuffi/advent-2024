input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def main() -> None:
    input = open("10.input").read()
    trail_map = [list(x) for x in input.split('\n')]
    trail_heads = [(x, y) for x in range(len(trail_map)) for y in range(len(trail_map[x])) if trail_map[x][y] == "0"]
    print(part1(trail_heads, trail_map))
    print(part2(trail_heads, trail_map))

def part1(trail_heads: list[tuple[int, int]], trail_map: list[list[str]]) -> int:
    return sum([walk_trail(trail_head, set(), trail_map) for trail_head in trail_heads])

def part2(trail_heads: list[tuple[int, int]], trail_map: list[list[str]]) -> int:
    return sum([walk_trail_2(trail_head, trail_map) for trail_head in trail_heads])


def walk_trail_2(curr_location: tuple[int, int], trail_map: list[list[str]]) -> int:
    directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    x, y = curr_location
    location_topology = int(trail_map[x][y])
    if location_topology == 9: 
        return 1
    good_directions = []
    for direction in directions:
        dx, dy = direction
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= len(trail_map) or new_y < 0 or new_y >= len(trail_map[x]):
            continue
        if int(trail_map[new_x][new_y]) == location_topology+1:
            good_directions.append((new_x, new_y))
    return sum([walk_trail_2(direction, trail_map) for direction in good_directions])


def walk_trail(curr_location: tuple[int, int], unique_nines: set[tuple[int, int]], trail_map: list[list[str]]) -> int:
    directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]
    x, y = curr_location
    location_topology = int(trail_map[x][y])
    if location_topology == 9: 
        if (x, y) not in unique_nines:
            unique_nines.add((x, y))
            return 1
        else:
            return 0
    good_directions = []
    for direction in directions:
        dx, dy = direction
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= len(trail_map) or new_y < 0 or new_y >= len(trail_map[x]):
            continue
        if int(trail_map[new_x][new_y]) == location_topology+1:
            good_directions.append((new_x, new_y))
    return sum([walk_trail(direction, unique_nines, trail_map) for direction in good_directions])
main()
