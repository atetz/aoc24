from utils.helpers import read_puzzle_input_as_string


def main():
    data = read_puzzle_input_as_string(
        11,
    )

    stones = [int(stone) for stone in data.split(" ")]
    print(stones)
    blinks = 25
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

    print(len(stones))


if __name__ == "__main__":
    main()
