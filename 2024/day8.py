from collections import defaultdict


def in_bounds(size, x, y):
    return 0 <= x < size[0] and 0 <= y < size[1]


def find_antinodes(antennas, size, resonant=False):
    antinodes = set()
    for ant_coords in antennas.values():
        for i, (x, y) in enumerate(ant_coords):
            for ox, oy in ant_coords[i + 1 :]:
                dx, dy = ox - x, oy - y
                xx, yy = (x, y) if resonant else (x - dx, y - dy)
                while in_bounds(size, xx, yy):
                    antinodes.add((xx, yy))
                    if not resonant:
                        break
                    xx -= dx
                    yy -= dy
                xx, yy = (ox, oy) if resonant else (ox + dx, oy + dy)
                while in_bounds(size, xx, yy):
                    antinodes.add((xx, yy))
                    if not resonant:
                        break
                    xx += dx
                    yy += dy
    return antinodes


def main():
    antennas = defaultdict(list)
    with open("inputs/day8.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]
        size = (len(lines), len(lines[0]))
        for x, line in enumerate(lines):
            for y, elem in enumerate(line):
                if elem != ".":
                    antennas[elem].append((x, y))

    # PART 1
    print(len(find_antinodes(antennas, size)))
    # PART 2
    print(len(find_antinodes(antennas, size, True)))


if __name__ == "__main__":
    main()
