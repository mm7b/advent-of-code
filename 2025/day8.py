from functools import reduce
from math import sqrt
from operator import itemgetter, mul


def get_distances(coordinates):
    dists = {}
    for i, (x, y, z) in enumerate(coordinates):
        for j, (a, b, c) in enumerate(coordinates):
            if i != j and (a, b, c, x, y, z) not in dists:
                dists[(x, y, z, a, b, c)] = sqrt(
                    (x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2
                )
    return [points for points, _ in sorted(dists.items(), key=itemgetter(1))]


def link(circuits, circuit, point):
    existing = [curr for curr in circuits if point in curr]
    if existing:
        circuits.append(circuit | existing[0])
        circuits.remove(existing[0])
    else:
        circuits.append(circuit | {point})
    circuits.remove(circuit)


def connect(coordinates, distances, nr_connections=0, end_all_connect=False):
    circuits = []
    for i in range(nr_connections or len(distances)):
        x, y, z, a, b, c = distances[i]
        added = False
        for circuit in circuits:
            if (x, y, z) in circuit and (a, b, c) in circuit:
                added = True
                break
            if (x, y, z) in circuit:
                link(circuits, circuit, (a, b, c))
                added = True
                break
            if (a, b, c) in circuit:
                link(circuits, circuit, (x, y, z))
                added = True
                break
        if not added:
            circuits.append({(x, y, z), (a, b, c)})
        elif (
            end_all_connect
            and len(circuits) == 1
            and len(circuits[0]) == len(coordinates)
        ):
            break
    return sorted(circuits, key=len, reverse=True), (x, a)


def main():
    with open("inputs/day8.txt", "r", encoding="utf8") as f:
        coordinates = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]
        distances = get_distances(coordinates)

    # PART 1
    circuits, _ = connect(coordinates, distances, 1000)
    print(reduce(mul, [len(c) for c in circuits[:3]]))

    # PART 2
    _, (x, a) = connect(coordinates, distances, end_all_connect=True)
    print(x * a)


if __name__ == "__main__":
    main()
