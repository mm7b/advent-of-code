import string


class Elf:
    def __init__(self, start: str, end: str) -> None:
        self.start = int(start)
        self.end = int(end)

    def __str__(self) -> str:
        return f"{self.start} -> {self.end}"

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end}"


def main():
    lines = []
    input_lines = []
    with open("inputs/day4.txt", "r", encoding="utf8") as f:
        input_lines = [l.strip() for l in f.readlines()]
        for line in input_lines:
            e1, e2 = line.split(",")
            lines.append((Elf(*e1.split("-")), Elf(*e2.split("-"))))

    tot = 0
    for e1, e2 in lines:
        # if e1.start <= e2.start and e1.end >= e2.end:
        #     tot += 1
        # elif e2.start <= e1.start and e2.end >= e1.end:
        #     tot += 1

        if e2.start <= e1.start <= e2.end:
            tot += 1
        elif e1.start <= e2.start <= e1.end:
            tot += 1
    print(tot)


if __name__ == "__main__":
    main()
