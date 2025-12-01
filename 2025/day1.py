from operator import add, sub


def main():
    with open("inputs/day1.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        rotations = [(add if l[0] == "R" else sub, int(l[1:])) for l in lines]

    # PART 1
    tot = 0
    nr = 50
    for op, val in rotations:
        nr = op(nr, val) % 100
        if nr == 0:
            tot += 1
    print(tot)

    # PART 2
    tot = 0
    nr = 50
    for op, val in rotations:
        tot += abs(val // 100)
        next_nr = op(nr, val) % 100
        if (
            (op == add and next_nr < nr)
            or next_nr == 0
            or (nr != 0 and op == sub and next_nr > nr)
        ):
            tot += 1
        nr = next_nr
    print(tot)


if __name__ == "__main__":
    main()
