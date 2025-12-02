def part1(ranges):
    valid_pw = []
    for start, end in ranges:
        current = range(start, end + 1)
        for pw in current:
            pw = str(pw)
            if len(pw) % 2 != 0:
                continue
            if pw[: len(pw) // 2] == pw[(len(pw) // 2) :]:
                valid_pw.append(int(pw))
    return sum(valid_pw)


def part2(ranges):
    valid_pw = []
    for start, end in ranges:
        current = range(start, end + 1)
        for pw in current:
            pw = str(pw)
            for i in range(1, (len(pw) // 2) + 1):
                slices = [pw[j : j + i] for j in range(0, len(pw), i)]
                if all(s == slices[0] for s in slices):
                    valid_pw.append(int(pw))
                    break
    return sum(valid_pw)


def main():
    with open("inputs/day2.txt", "r", encoding="utf8") as f:
        ranges = [tuple(map(int, l.split("-"))) for l in f.readline().split(",")]

    # PART 1
    # print(part1(ranges))

    # PART 2
    print(part2(ranges))


if __name__ == "__main__":
    main()
