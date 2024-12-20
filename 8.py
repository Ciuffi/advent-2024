from typing import Union, Tuple

input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
def main():
    input = open("8.input").read()
    location_map, xmax, ymax = get_map(input)
    print(part1(location_map, xmax, ymax))
    print(part2(location_map, xmax, ymax))

def get_map(input: str) -> dict[str, tuple[int, int]]:
    grid = [list(row) for row in input.strip().split('\n')]
    xmax = len(grid)
    ymax = len(grid[0])
    input_map = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] not in input_map:
                input_map[grid[x][y]] = []
            input_map[grid[x][y]].append((x, y))
    del input_map['.']
    return input_map, xmax, ymax

def part1(location_map: dict[str, tuple[int, int]], xmax: int, ymax: int):
    antinodes = {}
    for node, locations in location_map.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                location = locations[i]
                location2 = locations[j]
                new_antinodes = get_antinodes(location, location2)
                for antinode in new_antinodes:
                    if (check_antinodes(antinode, xmax, ymax)):
                        antinodes.setdefault(node, []).append(antinode)
    return len(set([item for sublist in antinodes.values() for item in sublist]))        

def get_all_antinodes(location: tuple[int, int], location2: tuple[int, int], xmax: int, ymax: int):
        antinodes = set()
        antinodes.add(location)
        antinodes.add(location2)
        curr_antinodes = location
        prev_antinode = location2
        while check_antinodes(curr_antinodes, xmax, ymax) or check_antinodes(prev_antinode, xmax, ymax):
            antinodes.add(curr_antinodes)
            atinode_temp = curr_antinodes
            curr_antinodes = get_antinodes(curr_antinodes, prev_antinode)[0]
            prev_antinode = atinode_temp
        curr_antinodes = location2
        prev_antinode = location
        while check_antinodes(curr_antinodes, xmax, ymax) or check_antinodes(prev_antinode, xmax, ymax):
            antinodes.add(curr_antinodes)
            atinode_temp = curr_antinodes
            curr_antinodes = get_antinodes(curr_antinodes, prev_antinode)[0]
            prev_antinode = atinode_temp
        return antinodes

              
def part2(location_map: dict[str, tuple[int, int]], xmax: int, ymax: int):
    antinodes = {}
    for node, locations in location_map.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                location = locations[i]
                location2 = locations[j]
                all_antinodes = get_all_antinodes(location, location2, xmax, ymax)
                all_antinodes = [antinode for antinode in all_antinodes if check_antinodes(antinode, xmax, ymax)]
                print("antinodes for location:", location, location2, "are:", all_antinodes)
                antinodes.setdefault(node, []).extend(all_antinodes)
    return len(set([item for sublist in antinodes.values() for item in sublist]))        

def check_antinodes(antinode: tuple[int, int], xmax: int, ymax: int) -> bool:
    if antinode[0] < 0 or antinode[0] > xmax -1 or antinode[1] < 0 or antinode[1] > ymax -1:
        return False
    return True

def get_antinodes(location: tuple[int, int], location2: tuple[int, int]) -> Union[tuple[int, int], tuple[int, int]]:
    xdiff, ydiff = get_distance(location, location2)
    antinode1 = [0, 0]
    antinode2 = [0, 0]
    if (location[0] > location2[0]):
        antinode1[0] = location[0] + xdiff
        antinode2[0] = location2[0] - xdiff
    else:
        antinode1[0] = location[0] - xdiff
        antinode2[0] = location2[0] + xdiff
    if (location[1] > location2[1]):
        antinode1[1] = location[1] + ydiff
        antinode2[1] = location2[1] - ydiff
    else:
        antinode1[1] = location[1] - ydiff
        antinode2[1] = location2[1] + ydiff
    return [tuple(antinode1), tuple(antinode2)]

def get_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> tuple[int, int]:
    return abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])
main()