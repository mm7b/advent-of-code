def get_adjacent_cells(matrix, r, c):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    cells = []
    for dr, dc in directions:
        if (
            0 <= r + dr < len(matrix)
            and 0 <= c + dc < len(matrix[0])
            and matrix[r + dr][c + dc]
        ):
            cells.append((r + dr, c + dc))
    return cells


def main():
    with open("inputs/day4.txt", "r", encoding="utf8") as f:
        matrix = [[1 if c == "@" else 0 for c in r.strip()] for r in f.readlines()]

    # PART 1
    accessible = []
    for r, row in enumerate(matrix):
        for c, elem in enumerate(row):
            if elem and len(get_adjacent_cells(matrix, r, c)) < 4:
                accessible.append((r, c))
    print(len(accessible))

    # PART 1 One-liner alternative
    print(
        len(
            [
                (r, c)
                for r, row in enumerate(matrix)
                for c, elem in enumerate(row)
                if elem
                and len(
                    [
                        (r + dr, c + dc)
                        for dr, dc in [
                            (-1, -1),
                            (-1, 0),
                            (-1, 1),
                            (0, -1),
                            (0, 1),
                            (1, -1),
                            (1, 0),
                            (1, 1),
                        ]
                        if 0 <= r + dr < len(matrix)
                        and 0 <= c + dc < len(matrix[0])
                        and matrix[r + dr][c + dc]
                    ]
                )
                < 4
            ]
        )
    )

    # PART 2
    total = 0
    while True:
        accessible = []
        for r, row in enumerate(matrix):
            for c, elem in enumerate(row):
                if elem and len(get_adjacent_cells(matrix, r, c)) < 4:
                    accessible.append((r, c))
        if not accessible:
            break
        total += len(accessible)
        for r, c in accessible:
            matrix[r][c] = 0
    print(total)


if __name__ == "__main__":
    main()
