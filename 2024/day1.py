from collections import Counter


def main():
    left, right = [], []
    with open("inputs/day1.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            l, r = line.strip().split()
            left.append(int(l))
            right.append(int(r))
    # PART 1
    left.sort()
    right.sort()
    distance = sum([abs(r - l) for (l, r) in zip(left, right)])
    print(distance)

    # PART 2
    right_counter = Counter(right)
    similarity = 0
    for l in left:
        similarity += l * right_counter.get(l, 0)
    print(similarity)


if __name__ == "__main__":
    main()
