from operator import add, mul


def find_operators(res, operands, operators=[add, mul]):
    for op in operators:
        val = op(operands[0], operands[1])
        if len(operands) > 2:
            if res_op := find_operators(res, [val] + operands[2:], operators):
                return res_op
        elif val == res:
            return True
    return False


def main():
    equations = []
    with open("inputs/day7.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            res, operands = line.strip().split(":")
            equations.append((int(res), [int(op) for op in operands.split()]))

    # PART 1
    print(sum([res for res, operands in equations if find_operators(res, operands)]))
    # PART 2
    print(
        sum(
            [
                res
                for res, operands in equations
                if find_operators(
                    res, operands, [add, mul, lambda x, y: int(str(x) + str(y))]
                )
            ]
        )
    )


if __name__ == "__main__":
    main()
