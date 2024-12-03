import re


def get_int(num: str) -> int:
    if not num:
        return None
    val = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }.get(num)
    return val if val else int(num)


def main():
    with open("inputs/day1.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]
    # lines = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]

    # Part 1
    # first_d = re.compile(r"\D*(\d)")
    # last_d = re.compile(r".*(\d+)(?!.*\d)")
    # tot = 0
    # for line in lines:
    #     first_n = first_d.search(line).group(1)
    #     last_n = last_d.search(line).group(1)
    #     number = int(first_n + last_n if last_n else first_n)
    #     tot += number
    # print(tot)

    # Part 2
    first_d = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
    last_d = re.compile(
        r".*(\d|one|two|three|four|five|six|seven|eight|nine)(?!.*\d|one|two|three|four|five|six|seven|eight|nine)"
    )
    tot = 0
    for line in lines:
        first_n = get_int(first_d.search(line).group(1))
        last_n = get_int(last_d.search(line).group(1))
        number = int(f"{first_n}{last_n}")
        print(line)
        print(first_n, last_n, number)
        print(first_d.search(line).group(1))
        print(first_d.search(line).group(0))
        input()
        tot += number
    print(tot)


if __name__ == "__main__":
    main()
