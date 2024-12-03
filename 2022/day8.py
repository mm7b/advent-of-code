class Tree:
    """Tree"""

    def __init__(self, height: int) -> None:
        self.height = height
        self.visible = False
        self.score = 1

    def __repr__(self) -> str:
        # return f"{'Visible' if self.visible else 'Unvisible'} Tree: {self.height}"
        return str(self.height)

    def __str__(self) -> str:
        # return f"{'Visible' if self.visible else 'Unvisible'} Tree: {self.height}"r
        return str(self.height)

    def __eq__(self, other: object) -> bool:
        return self.height == other.height

    def __lt__(self, other: object) -> bool:
        return self.height < other.height

    def __le__(self, other: object) -> bool:
        return self.height <= other.height


def main():
    with open("inputs/day8.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]

    max_row, max_col = (len(lines), len(lines[0]))
    print(max_row, max_col)
    # grid = [[None] * max_col] * max_row
    grid = []
    for i in range(max_row):
        row = []
        for j in range(max_col):
            row.append(None)
        grid.append(row)
    print(len(grid), len(grid[0]))

    for i, line in enumerate(lines):
        for j, height in enumerate(line):
            # try:
            grid[i][j] = Tree(int(height))
            # except IndexError:
            #     print(i, j, height)
            #     raise
    # grid_str = ["".join([str(o.height) for o in line]) for line in grid]
    # print("".join([str(t) for t in grid[-1]]))
    # print("".join([str(t) for t in grid[-2]]))
    # print("".join([str(t) for t in grid[66]]))
    # print(lines[0])

    for i, line in enumerate(grid):
        for j, tree in enumerate(line):
            if i == 0 or j == 0 or i == (max_row - 1) or j == (max_col - 1):
                tree.score = 0
                continue
            else:
                # up
                next_i = i - 1
                while next_i > 0:
                    if tree <= grid[next_i][j]:
                        break
                    next_i -= 1
                tree.score *= i - next_i

                # down
                next_i = i + 1
                while next_i < max_row - 1:
                    if tree <= grid[next_i][j]:
                        break
                    next_i += 1
                tree.score *= next_i - i

                # left
                next_j = j - 1
                while next_j > 0:
                    if tree <= grid[i][next_j]:
                        break
                    next_j -= 1
                tree.score *= j - next_j

                # right
                next_j = j + 1
                while next_j < max_col - 1:
                    if tree <= grid[i][next_j]:
                        break
                    next_j += 1
                tree.score *= next_j - j

    scores = []
    for line in grid:
        for tree in line:
            scores.append(tree.score)
    scores.sort(reverse=True)
    print(scores[0])


if __name__ == "__main__":
    main()
