from collections import defaultdict


def blink(stones, steps=25):
    for _ in range(steps):
        # Avoid updating
        new_stones = defaultdict(int)
        for s, n in stones.items():
            if s == 0:
                new_stones[1] += n
            elif len(ss := str(s)) % 2 == 0:
                new_stones[int(ss[: len(ss) // 2])] += n
                new_stones[int(ss[(len(ss) // 2) :])] += n
            else:
                new_stones[s * 2024] += n
        stones = new_stones
    return sum(stones.values())


def main():
    with open("inputs/day11.txt", "r", encoding="utf8") as f:
        lines = f.readline().strip()
        stones = {int(n): 1 for n in lines.split()}

    # PART 1
    print(blink(stones))
    # PART 2
    print(blink(stones, 75))


if __name__ == "__main__":
    main()
