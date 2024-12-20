def main():
    #get input from 2.input file
    with open('2.input') as f:
        reports = [line.split() for line in f]
    print("Part 1:",part1(reports))
    print("Part 2:",part2(reports))

def is_increasing_sequence(numbers: list[int]) -> bool:
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

def is_decreasing_sequence(numbers: list[int]) -> bool:
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            return False
    return True

def part1(reports: list[list[str]]) -> int:
    safe_reports = 0
    for report in reports:
        report = list(map(int, report))
        if check_safe(report):
            safe_reports += 1
    return safe_reports

def part2(reports: list[list[str]]) -> int:
    valid_reports = 0
    for report in reports:
        report = list(map(int, report))
        if check_safe(report):
            valid_reports += 1
            continue
        valid_with_dampener = False
        for i in range(len(report)):
            # Create a new list without the element at index i
            modified_report = [x for j, x in enumerate(report) if j != i]

            # Check if the modified report is valid
            if check_safe(modified_report):
                valid_with_dampener = True
                break
        if valid_with_dampener:
            valid_reports += 1
    return valid_reports

def check_safe(input_list: list[int]) -> bool:
    is_increasing = is_increasing_sequence(input_list)
    is_decreasing = is_decreasing_sequence(input_list)

    if not is_increasing and not is_decreasing:
        return False
    # Check that all adjacent levels differ by at least 1 and at most 3
    for i in range(len(input_list) - 1):
        diff = abs(input_list[i + 1] - input_list[i])
        if diff < 1 or diff > 3:
            return False
    return True
main()