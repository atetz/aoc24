import bisect
from collections import defaultdict
from typing import Dict, List

from utils.helpers import read_puzzle_input_as_string


def validate_page_order(pages: List[int], ordering_rules: Dict[int, List[int]]):
    for page in pages:
        # 75
        if ordering_rules[page]:
            # 75 [13, 29, 47, 53, 61]
            for rule in ordering_rules[page]:
                if rule in pages and pages.index(page) > pages.index(rule):
                    return False
    return True


def fix_pages_order(pages: List[int], ordering_rules: Dict[int, List[int]]):
    for page in pages:
        # 61
        if ordering_rules[page]:
            # 65 [13, 29, 53]
            for rule in ordering_rules[page]:
                # 13 = 1 in page
                if rule in pages and pages.index(page) > pages.index(rule):
                    pages.pop(pages.index(page))
                    pages.insert(pages.index(rule), page)
                    fix_pages_order(pages, ordering_rules)

    return pages


def main():
    page_ordering_rules = defaultdict(list)
    updates = []
    input = read_puzzle_input_as_string(5)
    for line in input.splitlines():
        if "|" in line:
            page, following_page = line.split("|")
            bisect.insort(page_ordering_rules[int(page)], int(following_page))
        if "," in line:
            bisect.insort(updates, ([int(page) for page in line.split(",")]))

    # correct_order = [75, 47, 61, 53, 29]
    # assert validate_page_order(correct_order, page_ordering_rules)

    # correct_order = [97, 61, 53, 29, 13]
    # assert validate_page_order(correct_order, page_ordering_rules)

    # correct_order = [75, 29, 13]
    # assert validate_page_order(correct_order, page_ordering_rules)

    # incorrect_order = [75, 97, 47, 61, 53]
    # assert not validate_page_order(incorrect_order, page_ordering_rules)

    # incorrect_order = [97, 13, 75, 29, 47]
    # assert not validate_page_order(incorrect_order, page_ordering_rules)

    # incorrect_order = [61, 13, 29]
    # assert not validate_page_order(incorrect_order, page_ordering_rules)

    correct_middle_page_sum = 0
    incorrect_middle_page_sum = 0
    for update in updates:
        if validate_page_order(update, page_ordering_rules):
            middle = update[int((len(update) - 1) / 2)]
            correct_middle_page_sum += middle
        else:
            fixed = fix_pages_order(update, page_ordering_rules)
            middle = fixed[int((len(fixed) - 1) / 2)]
            incorrect_middle_page_sum += middle

    print(correct_middle_page_sum)
    print(incorrect_middle_page_sum)


if __name__ == "__main__":
    main()
