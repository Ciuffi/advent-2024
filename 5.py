from typing import Union
import re

def main():
     input = open("5.input").read()
     rules, pages = sanatize_input(input)
     print("Part 1:",part1(rules, pages))
     print("Part 2:",part2(rules, pages))


def sanatize_input(input: str) -> Union[dict[str, str], list[list[str]]]:
    rules_map = {}
    [rules_map.setdefault(rule.split("|")[0], []).append(rule.split("|")[1]) for rule in re.findall(r"\d{2}\|\d{2}", input)]
    page_pattern = re.compile(r'^(?:\d{2}(?:,\d{2})*)$', re.MULTILINE)
    pages = page_pattern.findall(input)
    pages = [page.split(",") for page in pages]
    return rules_map, pages

def check_for_failure(rules: dict[str, str], pages: list[str]) -> bool:
        for i in range(len(pages)):
            if rules.get(pages[i]) is not None and any(item in pages[0:i] for item in rules.get(pages[i])):
                 return False
        return True

def part1(rules: dict[str, str], page_list: list[list[str]]) -> int:
    good_pages = [pages for pages in page_list if check_for_failure(rules, pages)]
    return sum([int(page[len(page) // 2]) for page in good_pages])

def swap_values(list: list[str], ind1: int, ind2: int) -> list[str]:
    list[ind1], list[ind2] = list[ind2], list[ind1]
    return list

def fix_page(rules: dict[str, str], pages: list[str]) -> list[str]:
    for i in range(len(pages) - 1, -1, -1):
        if check_for_failure(rules, pages) is False:
            for j in range(i - 1, -1, -1):
                if (rules.get(pages[i]) is None):
                     continue
                if pages[j] in rules.get(pages[i]):
                        pages = swap_values(pages, i, j)
    return pages

def part2(rules: dict[str, str], page_list: list[list[str]]) -> int:
     bad_pages = [pages for pages in page_list if not check_for_failure(rules, pages)]
     good_pages = [fix_page(rules, pages) for pages in bad_pages]
     return sum([int(page[len(page) // 2]) for page in good_pages])

main()