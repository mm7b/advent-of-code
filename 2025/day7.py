from collections import defaultdict


def find_splits(matrix, beams, splits=0, unique=True):
    new_beams = defaultdict(int)
    for (r, c), nr in beams.items():
        if r == len(matrix) - 1:
            continue
        if matrix[r + 1][c]:
            splits += 1 if unique else nr
            new_beams[(r + 1, c - 1)] += nr
            new_beams[(r + 1, c + 1)] += nr
        else:
            new_beams[(r + 1, c)] += nr
    return find_splits(matrix, new_beams, splits, unique) if new_beams else splits


def main():
    with open("inputs/day7.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        matrix = [[1 if c == "^" else 0 for c in r.strip()] for r in lines[1:]]
        beams = {(0, list(lines[0]).index("S")): 1}

    # PART 1
    print(find_splits(matrix, beams))

    # PART 2
    # Adding 1 "split" for the initial reality
    print(find_splits(matrix, beams, unique=False) + 1)


if __name__ == "__main__":
    main()
