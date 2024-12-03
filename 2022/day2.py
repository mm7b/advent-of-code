def transform(a, b):
    if b == "X":  # lose
        if a == "A":
            return "C"
        elif a == "B":
            return "A"
        elif a == "C":
            return "B"
    if b == "Y":  # draw
        return a
    if b == "Z":  # win
        if a == "A":
            return "B"
        elif a == "B":
            return "C"
        elif a == "C":
            return "A"

    # return {"X": "A", "Y": "B", "Z": "C"}[x]


def action_points(x):
    return {"A": 1, "B": 2, "C": 3}[x]


def score(x, y):
    if x == y:
        score = 3
    elif (x == "A" and y == "B") or (x == "B" and y == "C") or (x == "C" and y == "A"):
        score = 6
    else:
        score = 0
    return action_points(y) + score


def parse_input(filename):
    strategy = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                a, b = line.split()
                strategy.append((a, transform(a, b)))
    return strategy


def main():
    strategy = parse_input("inputs/day2.txt")
    total_score = 0
    for round in strategy:
        total_score += score(*round)
    print(total_score)


if __name__ == "__main__":
    main()
