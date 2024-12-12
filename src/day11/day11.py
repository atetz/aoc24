from typing import Dict, List, Tuple

from utils.helpers import read_puzzle_input_as_string


def bruteforce_count(stones: List[int], blinks: int):
    for blink in range(blinks):
        output = []
        for stone in stones:
            length = len(str(stone))
            if stone == 0:
                output.append(1)
                continue
            if length % 2 == 0:
                output.append(int(str(stone)[: length // 2]))
                output.append(int(str(stone)[length // 2 :]))
            else:
                output.append(stone * 2024)
        stones = output
    return stones


def cached_count(
    cache: Dict[Tuple[int, int], int], stone: List[int], blinks: int
) -> int:
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]
    if blinks == 0:
        return 1
    if stone == 0:
        result = cached_count(cache, 1, blinks - 1)
        cache[(stone, blinks)] = result
        return result
    length = len(str(stone))
    if length % 2 == 0:
        result = cached_count(
            cache, int(str(stone)[: length // 2]), blinks - 1
        ) + cached_count(cache, int(str(stone)[length // 2 :]), blinks - 1)
        cache[(stone, blinks)] = result
        return result

    result = cached_count(cache, stone * 2024, blinks - 1)
    cache[(stone, blinks)] = result
    return result


def count_stones(stones: List[int], blinks: int) -> int:
    cache = {}
    return sum(cached_count(cache, stone, blinks) for stone in stones)


def main():
    data = read_puzzle_input_as_string(11)
    stones = [int(stone) for stone in data.split(" ")]

    print(f"Part one: {count_stones(stones, 25)}")
    print(f"Part two: {count_stones(stones, 75)}")


if __name__ == "__main__":
    main()
