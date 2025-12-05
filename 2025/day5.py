def main():
    with open("inputs/day5.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]

    ranges = [tuple(map(int, l.split("-"))) for l in lines if "-" in l]
    ids = [int(l) for l in lines if l and "-" not in l]

    # PART 1
    print(len([i for i in ids if any(s <= i <= e for s, e in ranges)]))

    # PART 2
    total = 0
    # Sort by descending range size to avoid fully englobing ranges
    ranges = sorted(ranges, key=lambda r: r[1] - r[0], reverse=True)
    seen = set()
    for s, e in ranges:
        for other_s, other_e in seen:
            if s >= other_s and e <= other_e:
                s, e = 1, 0
                break
            if other_s <= s <= other_e:
                s = other_e + 1
            elif other_s <= e <= other_e:
                e = other_s - 1
        seen.add((s, e))
        total += e - s + 1
    print(total)


if __name__ == "__main__":
    main()
