LINEARS = [
    (1, 0),  # DOWN
    (-1, 0),  # UP
    (0, 1),  # RIGHT
    (0, -1),  # LEFT
]

DIAGONALS = [
    (1, 1),  # DOWN-RIGHT
    (1, -1),  # DOWN-LEFT
    (-1, 1),  # UP-RIGHT
    (-1, -1),  # UP-LEFT
]

ALL = LINEARS + DIAGONALS


def find_word(matrix, start_x, start_y, directions, word):
    centers = []
    for diff_x, diff_y in directions:
        x = start_x
        y = start_y
        curr = ""
        while len(curr) < len(word) and 0 <= x < len(matrix) and 0 <= y < len(matrix):
            curr += matrix[x][y]
            x += diff_x
            y += diff_y
        if curr == word:
            centers.append((start_x + diff_x, start_y + diff_y))  # A coords for X-MAS
    return centers


def part1(matrix):
    total = 0
    for x, line in enumerate(matrix):
        for y, char in enumerate(line):
            if char.upper() == "X":
                total += len(find_word(matrix, x, y, ALL, "XMAS"))
    return total


def part2(matrix):
    total = 0
    centers = set()
    for x, line in enumerate(matrix):
        for y, char in enumerate(line):
            if char.upper() == "M":
                new_centers = find_word(matrix, x, y, DIAGONALS, "MAS")
                for c in new_centers:
                    # Check if the newly found A coords have already been added
                    # If it is, it corresponds to an X-MAS
                    if c in centers:
                        total += 1
                centers |= set(new_centers)
    return total


def main():
    matrix = []
    with open("inputs/day4.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))
    # PART 1
    res = part1(matrix)
    print(res)

    # PART 2
    res = part2(matrix)
    print(res)


if __name__ == "__main__":
    main()
