import time
from functools import reduce


def main():
    # bag = {"red": 12, "green": 13, "blue": 14}
    # possible_games = []
    game_powers = 0
    with open("inputs/day2.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            i, sets = line.split(":")
            # game_id = int(i.split()[1])
            # stop = False
            min_bag = {"red": 0, "green": 0, "blue": 0}
            for s in sets.split(";"):
                for cube in s.strip().split(","):
                    nr, color = cube.strip().split()
                    if min_bag.get(color) < int(nr):
                        # if bag.get(color) < int(nr):
                        # stop = True
                        min_bag[color] = int(nr)
                        # break
                # if stop:
                # break
            # if not stop:
            # possible_games.append(game_id)
            # print(f"{line}\n{min_bag=}\n\n")
            game_powers += reduce(lambda x, y: x * y, min_bag.values())

    # print(sum(possible_games))
    print(game_powers)


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter() - start
    print(f"Took {end}s")
