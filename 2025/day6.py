from functools import reduce
from operator import add, mul


def main():
    # PART 1
    with open("inputs/day6.txt", "r", encoding="utf8") as f:
        problems = [
            [
                add if arg == "+" else mul if arg == "*" else int(arg)
                for arg in l.strip().split(" ")
                if arg
            ]
            for l in f.readlines()
        ]
    print(
        sum(
            [
                reduce(problems[-1][i], [arg[i] for arg in problems[:-1]])
                for i in range(len(problems[0]))
            ]
        )
    )

    # PART 2
    with open("inputs/day6.txt", "r", encoding="utf8") as f:
        matrix = [list(r.rstrip("\n")) for r in f.readlines()]

    operators = [add if c == "+" else mul for c in matrix[-1] if c.strip()]
    matrix = matrix[:-1]
    total = 0
    args = []
    for col in range(len(matrix[0])):
        arg = "".join(row[col] for row in matrix).strip()
        if arg:
            args.append(int(arg))
        if not arg or col == len(matrix[0]) - 1:
            total += reduce(operators.pop(0), args)
            args = []
    print(total)


if __name__ == "__main__":
    main()
