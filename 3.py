import re

def main():
    text = open('3.input').read()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'
    matches = re.findall(pattern, text)    # Process the matches
    print("Part 1:",part1(matches))
    print("Part 2:",part2(matches))

def part2(matches: list[str]) -> int:
    total = 0
    enabled = True
    for match in matches:
        if (match[2]):
            enabled = True
        elif (match[3]):
            enabled = False
        else:
            num1 = match[0]
            num2 = match[1]
            result = int(num1) * int(num2)
            total+= result if enabled else 0
    return total

def part1(matches: list[str]) -> int:
    return sum([int(match[0]) * int(match[1]) for match in matches if match[0] ])

main()