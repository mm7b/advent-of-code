DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)


def update_direction(dx, dy):
    return {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[(dx, dy)]


def in_bounds(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def get_start_coord(matrix):
    for x, line in enumerate(matrix):
        for y, col in enumerate(line):
            if col == "^":
                return (x, y)


def get_path(matrix, start, dx, dy):
    visited = set()
    loop = False
    x, y = start
    while True:
        visited.add((x, y, dx, dy))
        if not in_bounds(matrix, x + dx, y + dy):
            break
        elif matrix[x + dx][y + dy] == "#":
            dx, dy = update_direction(dx, dy)
        else:
            x += dx
            y += dy
            if (x, y, dx, dy) in visited:
                loop = True
                break
    return visited, loop


def part2_unoptimized(matrix, start, path):
    obstructions = set()
    for x, y, _, _ in path:
        if (x, y) == start:
            continue
        matrix[x][y] = "#"
        # Unoptimzed = check if the whole path from the beginning is a loop
        _, loop = get_path(matrix, start, -1, 0)
        if loop:
            obstructions.add((x, y))
        matrix[x][y] = "."
    return obstructions


def part2(matrix, start, path):
    obstructions = set()
    for x, y, dx, dy in path:
        if (x, y) == start or (x, y) in obstructions:
            continue
        matrix[x][y] = "#"
        # Only check if the path starting at the previous step is a loop
        new_start = (x - dx, y - dy)
        _, loop = get_path(matrix, new_start, dx, dy)
        if loop:
            obstructions.add((x, y))
        matrix[x][y] = "."
    return obstructions


def main():
    matrix = []
    with open("inputs/day6.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            matrix.append(list(line.strip()))

    start = get_start_coord(matrix)
    # PART 1
    path, _ = get_path(matrix, start, *UP)
    print(len(set([(x, y) for (x, y, _, _) in path])))

    # PART 2
    p2 = part2(matrix, start, path)
    print(len(p2))

    p2_uo = part2_unoptimized(matrix, start, path)
    print(len(p2_uo))


if __name__ == "__main__":
    main()
