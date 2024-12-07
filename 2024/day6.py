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
    visited = {}
    loop = False
    x, y = start
    i = 0
    while True:
        visited[(x, y, dx, dy)] = i  # Step index to later sort the cells visited
        i += 1
        if not in_bounds(matrix, x + dx, y + dy):
            break
        if matrix[x + dx][y + dy] == "#":
            dx, dy = update_direction(dx, dy)
        else:
            x += dx
            y += dy
            if (x, y, dx, dy) in visited:
                loop = True
                break
    return visited, loop


def part2(matrix, start, path):
    obstructions = {}
    # Sorting the visited cell to only check the first time the path reaches the current cell
    for x, y, dx, dy in sorted(path, key=lambda x: path[x]):
        if (x, y) == start or (x, y) in obstructions:
            continue
        matrix[x][y] = "#"
        # Only check if the path starting at the previous step is a loop
        new_start = (x - dx, y - dy)
        _, loop = get_path(matrix, new_start, dx, dy)
        obstructions[(x, y)] = loop
        matrix[x][y] = "."
    return [coord for coord, loop in obstructions.items() if loop]


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


if __name__ == "__main__":
    main()
