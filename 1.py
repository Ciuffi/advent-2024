from collections import Counter
from typing import Union

def main():
    input = open('1.input').readlines()
    list1, list2 = process_data(input)
    print("Part 1:",part1(list1, list2))
    print("Part 2:",part2(list1, list2))

def process_data(input: list[str]) -> Union[list[int], list[int]]:
    list1 = [line.split()[0] for line in input]
    list2 = [line.split()[1] for line in input]
    list1.sort()
    list2.sort()
    list1 = [int(a) for a in list1]
    list2 = [int(a) for a in list2]
    return list1, list2

def part1(list1: list[int], list2: list[int]) -> int:
    return sum([abs(list1[i]-list2[i]) for i in range(len(list1))])

def part2(list1: list[int], list2: list[int]) -> int:
    c = Counter(list2)
    return sum(i * c.get(i, 0) for i in list1)

main()