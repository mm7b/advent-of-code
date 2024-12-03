def is_valid_part1(report):
    increasing = (report[1] - report[0]) > 0
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if (
            diff == 0
            or abs(diff) > 3
            or (increasing and diff < 0)
            or (not increasing and diff > 0)
        ):
            return False
    return True


def is_valid_part2(report, removed=False):
    increasing = (report[1] - report[0]) > 0
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if (
            diff == 0
            or abs(diff) > 3
            or (increasing and diff < 0)
            or (not increasing and diff > 0)
        ):
            return (
                False
                if removed
                else (
                    is_valid_part2(report[:i] + report[i + 1 :], True)
                    or is_valid_part2(report[: i + 1] + report[i + 2 :], True)
                    or (
                        i == 1 and is_valid_part2(report[: i - 1] + report[i:], True)
                    )  # only when the second digit might have impacted the increasing/decreasing variable
                )
            )
    return True


def main():
    reports = []
    with open("inputs/day2.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            reports.append([int(l) for l in line.strip().split()])
    # PART 1
    valid_reports = [r for r in reports if is_valid_part1(r)]
    print(len(valid_reports))

    # PART 2
    valid_reports = [r for r in reports if is_valid_part2(r)]
    print(len(valid_reports))


if __name__ == "__main__":
    main()
