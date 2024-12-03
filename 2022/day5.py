class Grid:
    def __init__(self, input_lines):
        self.structure = [None] * len(input_lines[8].strip().split("   "))

        for j in range(7, -1, -1):
            for i in range(9):
                val = input_lines[j][i * 4 + 1]
                if val.strip():
                    line = self.structure[i] if j < 7 else []
                    line.append(val)
                    self.structure[i] = line

        print(self.structure)

    def __repr__(self) -> str:
        build_str = ""
        max_line_length = max([len(line) for line in self.structure])
        length = len(self.structure)
        j = length - 1
        while j >= 0:
            for i in range(length):
                build_str += (
                    f"[{self.structure[i][j]}]" if j < len(self.structure[i]) else "   "
                )
                build_str += " "
            build_str += "\n"
            j -= 1
        build_str += " "
        build_str += "   ".join([str(o + 1) for o in range(len(self.structure))])
        return build_str


class Container:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Action:
    def __init__(self, nr: str, start: str, end: str) -> None:
        self.nr = int(nr)
        self.start = int(start)
        self.end = int(end)

    def __str__(self) -> str:
        return f"{self.start} -> {self.end} x{self.nr}"

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end} x{self.nr}"


def main():
    actions = []

    input_lines = []
    with open("inputs/day5.txt", "r", encoding="utf8") as f:
        input_lines = [l for l in f.readlines()]
        grid = Grid(input_lines)

        print(grid)
        for action in input_lines[10:]:
            nr = int(action.split()[1])
            source = int(action.split()[3]) - 1
            to = int(action.split()[5]) - 1
            actions.append(Action(nr, source, to))

    for i, action in enumerate(actions):
        print(f"Action nr: {i+1} / {len(actions)}", end="\r")
        """while action.nr > 0:
            source = grid.structure[action.start]
            dest = grid.structure[action.end]
            dest.append(source.pop())
            grid.structure[action.start] = source
            grid.structure[action.end] = dest
            action.nr -= 1"""
        source = grid.structure[action.start]
        dest = grid.structure[action.end]
        to_take = len(source) - action.nr
        dest.extend(source[to_take:])
        source = source[:to_take]
        grid.structure[action.start] = source
        grid.structure[action.end] = dest

    # return
    print(grid)
    res = ""
    for line in grid.structure:
        res += line[-1]
    print(res)


if __name__ == "__main__":
    main()
