from utils.helpers import read_puzzle_input_as_single_line_string

# inspired by HyperNeutrino


def part_one(data: str) -> int:
    disk = []
    file_id = 0
    for id, char in enumerate(data):
        size = int(char)
        if id % 2 == 0:
            disk += [file_id] * size
            file_id += 1
        else:  # blanks are represented as -1
            disk += [-1] * size

    # returns id of blanks (-1)
    blanks = [i for i, x in enumerate(disk) if x == -1]

    for i in blanks:
        while disk[-1] == -1:
            disk.pop()
        if len(disk) <= i:
            break
        disk[i] = disk.pop()

    return sum(i * x for i, x in enumerate(disk))


def part_two(data: str) -> int:
    files = {}
    blanks = []
    file_id = 0
    pos = 0
    for id, char in enumerate(data):
        size = int(char)
        if id % 2 == 0:
            if size == 0:
                raise ValueError("Unexpected 0 size for file.")
            files[file_id] = (pos, size)
            file_id += 1
        else:
            if size != 0:
                blanks.append((pos, size))
        pos += size

    while file_id > 0:
        file_id -= 1
        pos, size = files[file_id]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[file_id] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break
    total = 0

    for file_id, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += file_id * x
    return total


def main() -> None:
    data = read_puzzle_input_as_single_line_string(
        9,
    )

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main()
