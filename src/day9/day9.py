from collections import defaultdict
from typing import Dict, List

from utils.helpers import read_puzzle_input_as_single_line_string


def fragment_disk(disk_map: str) -> List[str]:
    result = []
    file_id = 0
    for pos, value in enumerate(disk_map):
        is_file = (pos % 2) == 0
        for i in range(int(value)):
            result.append(f"{file_id}" if is_file else ".")
        if is_file:
            file_id += 1
    return result


def rearrange_fragments(disk: List[str]) -> List[str]:
    file_parts = [file for file in disk if file != "."]
    for id, val in enumerate(disk):
        if val == ".":
            file_parts.insert(id, file_parts[-1])
            file_parts.pop(-1)
    return file_parts


def calculate_hash(fragments: List[str]) -> int:
    total = 0
    for i in range(len(fragments)):
        if fragments[i] == ".":
            continue
        total += i * int(fragments[i])
    return total


def get_file_sizes(fragmented_disk: List[str]) -> Dict[int, int]:
    # fragment id, size
    fragment_size_map = defaultdict(int)
    for fragment in fragmented_disk:
        if fragment.isdigit():
            fragment_size_map[fragment] += 1
    return fragment_size_map


def solve_part_one(data: str) -> int:
    disk = fragment_disk(data)
    arranged_disk = rearrange_fragments(disk)
    return calculate_hash(arranged_disk)


def get_empty_sectors(fragmented_disk: List[str]) -> Dict[int, int]:
    empty_sectors = defaultdict(int)  # position, size
    start_index = None

    for id, fragment in enumerate(fragmented_disk):
        if fragment == ".":
            if start_index is None:
                start_index = id
                empty_sectors[start_index] = 1
            else:
                empty_sectors[start_index] += 1
        else:
            start_index = None
    return empty_sectors


def defragment_disk(disk: List[str]) -> List[str]:
    file_sizes = get_file_sizes(disk)
    file_ids = set(int(fragment) for fragment in disk if fragment != ".")

    for i in range(len(file_ids) - 1):
        file_id = max(file_ids)
        file_size = file_sizes[str(file_id)]
        empty_sectors = get_empty_sectors(disk)
        for index, size in sorted(empty_sectors.items()):
            if file_size <= size and disk.index(str(file_id)) >= index:
                disk = ["." if x == str(file_id) else x for x in disk]
                for i in range(file_size):
                    disk.pop(index + (file_size - 1))
                    disk.insert(index, str(file_id))
                break
        file_ids.discard(file_id)
    return disk


def solve_part_two(data: str) -> int:
    fragments = fragment_disk(data)
    disk = defragment_disk(fragments)
    return calculate_hash(disk)


def main() -> None:
    data = read_puzzle_input_as_single_line_string(9, True)
    print(f"part one: {solve_part_one(data)}")
    print(f"part two: {solve_part_two(data)}")


if __name__ == "__main__":
    main()
