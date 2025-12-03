from operator import itemgetter


def find_batteries(banks, size):
    packs = []
    for bank in banks:
        pack = ""
        for i in range(size):
            max_i, max_val = max(
                enumerate(bank[: len(bank) - (size - i - 1)]), key=itemgetter(1)
            )
            pack += max_val
            bank = bank[max_i + 1 :]
        packs.append(int(pack))
    return sum(packs)


def main():
    with open("inputs/day3.txt", "r", encoding="utf8") as f:
        banks = [l.strip() for l in f.readlines()]

    # PART 1
    print(find_batteries(banks, 2))

    # PART 2
    print(find_batteries(banks, 12))


if __name__ == "__main__":
    main()
