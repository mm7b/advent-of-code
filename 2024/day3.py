import re


def extract_digit(instructions, index):
    number = ""
    try:
        while instructions[index].isdigit():
            number += instructions[index]
            index += 1
        if len(number) > 3:
            return None, index
        return int(number), index
    # Index could be out of range when the string ends in a number being parsed
    except IndexError:
        return None, index


def part2(instructions):
    total = 0
    do = True
    i = 0
    while i < len(instructions):
        if instructions[i : i + 4] == "mul(" and do:
            left, i = extract_digit(instructions, i + 4)
            if not left or instructions[i] != ",":
                continue
            right, i = extract_digit(instructions, i + 1)
            if not right or instructions[i] != ")":
                continue
            total += left * right
        elif instructions[i : i + 4] == "do()":
            do = True
            i += 4
        elif instructions[i : i + 7] == "don't()":
            do = False
            i += 7
        else:
            i += 1
    return total


def main():
    instructions = ""
    with open("inputs/day3.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            instructions += line.strip()
    # PART 1
    res = sum(
        [
            int(a) * int(b)
            for (a, b) in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)
        ]
    )
    print(res)

    # PART 2
    res = part2(instructions)
    print(res)


if __name__ == "__main__":
    main()
