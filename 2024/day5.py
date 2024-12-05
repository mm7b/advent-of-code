def is_valid(precedences, update):
    seen = set()
    for page in update:
        if any([after in seen for after in precedences.get(page, [])]):
            return False
        seen.add(page)
    return True


def reorder(precedences, update):
    for i, page in enumerate(update):
        while any([item in precedences.get(page, []) for item in update[:i]]):
            update.insert(i - 1, update.pop(i))
            i = i - 1
    return update


def main():
    precedences = {}
    updates = []
    with open("inputs/day5.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            elif "|" in line:
                prev, after = (int(x) for x in line.split("|"))
                afters = precedences.get(prev, set())
                afters.add(after)
                precedences[prev] = afters
            else:
                updates.append([int(x) for x in line.split(",")])

    # PART 1
    res = sum(
        [
            update[len(update) // 2]
            for update in updates
            if is_valid(precedences, update)
        ]
    )
    print(res)

    # PART 2
    res = sum(
        [
            reorder(precedences, update)[len(update) // 2]
            for update in updates
            if not is_valid(precedences, update)
        ]
    )
    print(res)


if __name__ == "__main__":
    main()
