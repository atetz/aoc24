from typing import List


def read_puzzle_input(filename: str) -> List[str]:
    with open(filename) as f:
        lines = f.read()
        return lines
