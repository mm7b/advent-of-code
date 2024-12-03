import operator


class Action:
    def __init__(self, direction, nr) -> None:
        self.direction = direction
        self.nr = nr

    def apply(self):
        res = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}[self.direction]
        self.nr -= 1
        return res


def get_adjacent_move(h_pos, t_pos) -> bool:
    h_row, h_col = h_pos
    t_row, t_col = t_pos
    r_diff = h_row - t_row
    c_diff = h_col - t_col
    if abs(r_diff) <= 1 and abs(c_diff) <= 1:
        return None
    r_mod = 0
    c_mod = 0
    if r_diff > 1:
        r_mod += 1
        if c_diff > 0:
            c_mod += 1
        elif c_diff < 0:
            c_mod -= 1
    elif r_diff < -1:
        r_mod -= 1
        if c_diff > 0:
            c_mod += 1
        elif c_diff < 0:
            c_mod -= 1
    elif c_diff > 1:
        c_mod += 1
        if r_diff > 0:
            r_mod += 1
        elif r_diff < 0:
            r_mod -= 1
    elif c_diff < -1:
        c_mod -= 1
        if r_diff > 0:
            r_mod += 1
        elif r_diff < 0:
            r_mod -= 1
    return (r_mod, c_mod)


def main():
    with open("inputs/day9.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]

    actions = []
    for line in lines:
        d, n = line.strip().split()
        actions.append(Action(d, int(n)))

    visited = set()
    h_pos = (0, 0)
    others = []
    for _ in range(9):
        others.append((0, 0))
    t_pos = (0, 0)
    visited.add(t_pos)

    for action in actions:
        while action.nr > 0:
            # Get action
            action_mov = action.apply()
            # Move head
            h_pos = tuple(map(operator.add, h_pos, action_mov))
            # Move knot 1 -> 9
            for i, other in enumerate(others):
                new_pos_move = get_adjacent_move(
                    others[i - 1] if i > 0 else h_pos, other
                )
                if new_pos_move:
                    new_pos = tuple(map(operator.add, other, new_pos_move))
                    others[i] = new_pos
            # Check for new pos for tail
            new_pos_move = get_adjacent_move(others[-1], t_pos)
            if new_pos_move:
                # input(f"{h_pos=} \n {others} \n {t_pos} -> {new_pos_move}")
                new_pos = tuple(map(operator.add, t_pos, new_pos_move))
                visited.add(new_pos)
                t_pos = new_pos

    print(len(visited))


if __name__ == "__main__":
    main()
