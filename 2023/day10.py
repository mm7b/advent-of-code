"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
"""


def connections(pipe):
    return {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
    }[pipe]


DIRECTIONS = [
    (1, 0),  # DOWN
    (-1, 0),  # UP
    (0, 1),  # RIGHT
    (0, -1),  # LEFT
]


def in_bounds(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def get_start_coord(matrix):
    for x, line in enumerate(matrix):
        for y, col in enumerate(line):
            if col == "S":
                return (x, y)


def get_loop_dfs(matrix, start, direction):
    start_x, start_y = start
    loop = [start]
    dir_x, dir_y = direction
    x = start_x + dir_x
    y = start_y + dir_y
    while (x, y) != (start_x, start_y) and in_bounds(matrix, x, y):
        # print(f"Current loop: {loop} -> reading {matrix[x][y]} at {(x, y)}")
        if matrix[x][y] == ".":
            break
        conns = connections(matrix[x][y])
        if (x + conns[0][0], y + conns[0][1]) == loop[-1]:
            loop.append((x, y))
            x += conns[1][0]
            y += conns[1][1]
        elif (x + conns[1][0], y + conns[1][1]) == loop[-1]:
            loop.append((x, y))
            x += conns[0][0]
            y += conns[0][1]
        else:
            break
    if (x, y) == (start_x, start_y):
        return loop
    return []


def inside_loop(matrix, point, loop):
    if point in loop:
        return False
    intersections = 0
    x, y = (point[0], 0)
    diff_x, diff_y = (0, 1)
    while (x, y) != point:
        if (x, y) in loop and matrix[x][y] != "-":
            intersections += 1
        x += diff_x
        y += diff_y
    if intersections % 2 == 0:
        return False
    # Make sure it still touches the polygone before going out of bounds
    while in_bounds(matrix, x, y):
        x += diff_x
        y += diff_y
        if (x, y) in loop:
            return True
    return False


def print_loop(matrix, loop):
    for x, line in enumerate(matrix):
        line_str = ""
        for y, elem in enumerate(line):
            line_str += f"{elem if (x, y) in loop else '.'} "
        print(f"{line_str}\n")


def part1(matrix, start):
    for direction in DIRECTIONS:
        l = get_loop_dfs(matrix, start, direction)
        if l:
            return len(l) // 2 + len(l) % 2
    return 0


def part2(matrix, start):
    for direction in DIRECTIONS:
        if loop := get_loop_dfs(matrix, start, direction):
            break

    print_loop(matrix, loop)
    min_x = min([x for (x, _) in loop])
    max_x = max([x for (x, _) in loop])
    min_y = min([y for (_, y) in loop])
    max_y = max([y for (_, y) in loop])
    points = [
        (x, y)
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
        if inside_loop(matrix, (x, y), loop)
    ]
    print(points)
    print(f"Errors: {[p for p in points if matrix[p[0]][p[1]] != 'I']}")
    return len(points)


def main():
    with open("inputs/day10_l.txt", "r", encoding="utf8") as f:
        matrix = [list(line.strip()) for line in f.readlines()]

    start = get_start_coord(matrix)
    # PART 1
    print(part1(matrix, start))

    # PART 2
    print(part2(matrix, start))


if __name__ == "__main__":
    main()
