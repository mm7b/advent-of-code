from operator import itemgetter

from shapely.geometry import Polygon


def main():
    with open("inputs/day9.txt", "r", encoding="utf8") as f:
        coordinates = [
            tuple(map(int, l.strip().split(",")[::-1])) for l in f.readlines()
        ]

    # PART 1
    areas = {}
    for i, (x, y) in enumerate(coordinates):
        for j, (a, b) in enumerate(coordinates):
            if i != j and (a, b, x, y) not in areas:
                areas[(x, y, a, b)] = ((x - a if x > a else a - x) + 1) * (
                    (y - b if y > b else b - y) + 1
                )
    print(max(areas.values()))

    # PART 2
    polygon = Polygon(coordinates)
    areas_lst = sorted(areas.items(), key=itemgetter(1), reverse=True)
    for (x, y, a, b), area in areas_lst:
        if polygon.contains(Polygon([(x, y), (x, b), (a, b), (a, y)])):
            print(area)
            break


if __name__ == "__main__":
    main()
