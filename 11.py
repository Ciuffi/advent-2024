input = "125 17"

def main() -> None:
    input = open("11.input").read()
    input = [int(x) for x in input.split(" ")]
    print("Starting input:", input)
    print("Part1:",  part1(input))
    print("Part2:", part2(input))

def part1(input: list[int]) -> int:
        return sum([run_iteration_recurse(num, 25, {}) for num in input])

def part2(input: list[int]) -> int:
        return sum([run_iteration_recurse(num, 75, {}) for num in input])

def run_iteration_recurse(value: int, level: int, mem: dict[tuple[int, int], int]):
    if (value, level) in mem:
        return mem[(value, level)]
    if level == 0:
        return 1
    if value == 0:
        result = run_iteration_recurse(1, level-1, mem)
    elif len(str(value)) % 2 == 0:
        val_str = str(value)
        mid = len(val_str) // 2
        result = run_iteration_recurse(int(val_str[:mid]), level-1, mem) + run_iteration_recurse(int(val_str[mid:]), level-1, mem)
    else:
        result = run_iteration_recurse(value * 2024, level-1, mem)
    mem[(value, level)] = result
    return result
    
main()