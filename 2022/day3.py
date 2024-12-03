import string


def index(x):
    return string.ascii_letters.index(x) + 1


def main():
    lines = []
    with open("inputs/day3.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]

    # for line in lines:
    #     mid = len(line) // 2
    #     lines.append((line[:mid], line[mid:]))

    tot = 0
    # for start, end in lines:
    #     tot += index(set(start).intersection(end).pop())
    for start in list(range(len(lines)))[::3]:
        tot += index(
            set(lines[start])
            .intersection(set(lines[start + 1]).intersection(set(lines[start + 2])))
            .pop()
        )
    print(tot)


if __name__ == "__main__":
    main()
