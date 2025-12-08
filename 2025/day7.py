from collections import defaultdict


def find_timelines(matrix, beams, timelines=1):
    new_beams = defaultdict(int)
    for (r, c), nr in beams.items():
        if r == len(matrix) - 1:
            continue
        if matrix[r + 1][c]:
            timelines += 1 * nr
            new_beams[(r + 1, c - 1)] += nr
            new_beams[(r + 1, c + 1)] += nr
        else:
            new_beams[(r + 1, c)] += nr
    return find_timelines(matrix, new_beams, timelines) if new_beams else timelines


def main():
    with open("inputs/day7.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        matrix = [[1 if c == "^" else 0 for c in r.strip()] for r in lines[1:]]

    # PART 1
    beams = {(0, list(lines[0]).index("S"))}
    splits = 0
    while beams:
        new_beams = set()
        for r, c in beams:
            if r == len(matrix) - 1:
                continue
            if matrix[r + 1][c]:
                splits += 1
                new_beams.update([(r + 1, c - 1), (r + 1, c + 1)])
            else:
                new_beams.add((r + 1, c))
        beams = new_beams
    print(splits)

    # PART 2
    beams = {(0, list(lines[0]).index("S")): 1}
    print(find_timelines(matrix, beams))


if __name__ == "__main__":
    main()
