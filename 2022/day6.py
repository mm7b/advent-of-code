def main():
    line = []
    with open("inputs/day6.txt", "r", encoding="utf8") as f:
        line = [l.strip() for l in f.readlines()]

    if len(line) != 1:
        return
    line = line[0]

    buffer = []
    res = None
    for i, val in enumerate(line):
        buffer.append(val)
        if i >= 13:
            if i > 13:
                buffer.pop(0)
            if len(set(buffer)) == 14:
                res = i + 1
                break
    print(res)


if __name__ == "__main__":
    main()
