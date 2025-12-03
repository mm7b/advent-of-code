def find_batteries(banks, size):
    packs = []
    for bank in banks:
        pack = [0] * size
        for i, battery in enumerate(bank):
            for j in range(0, min(i + 1, size)):
                if battery > pack[j] and len(bank) - i >= len(pack) - j:
                    pack[j] = battery
                    pack[j + 1 :] = [0] * (len(pack) - (j + 1))
                    break
        packs.append(int("".join(str(b) for b in pack)))
    return sum(packs)


def main():
    with open("inputs/day3.txt", "r", encoding="utf8") as f:
        banks = [[int(b) for b in line.strip()] for line in f.readlines()]

    # PART 1
    print(find_batteries(banks, 2))

    # PART 2
    print(find_batteries(banks, 12))


if __name__ == "__main__":
    main()
