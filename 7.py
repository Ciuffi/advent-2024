input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def main():
     input = open("7.input").read()
     tests = {int(line.split(":")[0]): [x for x in map(int, line.split(": ")[1].split(" "))] for line in input.splitlines()}
     print("Part 1: ", part1(tests))
     print("Part 2: ", part2(tests))

def concate(num1: int, num2: int) -> int:
     return int(str(num1) + str(num2))

def part1(tests: dict[int, list[int]]) -> int:
    return sum([k for k, v in tests.items() if find_stuff(k, v)])

def part2(tests: dict[int, list[int]]) -> int:
    return sum([k for k, v in tests.items() if find_stuff(k, v, True)])

def find_stuff(test: int, numbers: list[int], concat: bool=False, index: int=0, value: int=0) -> bool:
    if index == len(numbers):
            return value == test
    if index == 0:
        return find_stuff(test, numbers, concat, index + 1, numbers[index])
    return (find_stuff(test, numbers, concat, index + 1, value * numbers[index]) or 
                find_stuff(test, numbers, concat, index + 1, value + numbers[index]) or 
                (find_stuff(test, numbers, concat, index + 1, concate(value, numbers[index])) if concat else False))

main()