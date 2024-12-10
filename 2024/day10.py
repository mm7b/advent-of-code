DIRECTIONS = [
    (-1, 0),  # UP
    (0, 1),  # RIGHT
    (1, 0),  # DOWN
    (0, -1),  # LEFT
]


def get_heads(matrix):
    return [
        (x, y)
        for x, line in enumerate(matrix)
        for y, height in enumerate(line)
        if not height
    ]


def in_bounds(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def get_trails(matrix, start, distinct=True):
    seen = set()
    trails = 0
    queue = [(*start, 0)]
    while queue:
        x, y, h = queue.pop(0)  # breadth first search
        if distinct and (x, y) in seen:
            continue
        seen.add((x, y))
        if matrix[x][y] == 9:
            trails += 1
            continue
        queue.extend(
            [
                (x + dx, y + dy, h + 1)
                for (dx, dy) in DIRECTIONS
                if in_bounds(matrix, x + dx, y + dy) and matrix[x + dx][y + dy] == h + 1
            ]
        )
    return trails


def main():
    matrix = []
    with open("inputs/day10.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            matrix.append([int(h) for h in list(line.strip())])

    # PART 1
    print(sum([get_trails(matrix, start) for start in get_heads(matrix)]))
    # PART 2
    print(
        sum([get_trails(matrix, start, distinct=False) for start in get_heads(matrix)])
    )


if __name__ == "__main__":
    main()
