from uuid import uuid4


class Elf:
    def __init__(self, meals):
        self.id = str(uuid4())
        self.meals = meals
        self.total_calories = sum(meals)

    def __eq__(self, other):
        return self.id == other.id

    def __le__(self, other):
        return self.total_calories <= other.total_calories

    def __lt__(self, other):
        return self.total_calories < other.total_calories

    def __gt__(self, other):
        return self.total_calories > other.total_calories

    def __ge__(self, other):
        return self.total_calories >= other.total_calories

    def __str__(self):
        return f"Elf({self.id}) : {self.total_calories}"


def parse_input(filepath):
    elves = []
    with open(filepath, "r") as f:
        current_meals = []
        for line in f.readlines():
            line = line.strip()
            if line:
                current_meals.append(int(line))
            else:
                if current_meals:
                    elves.append(Elf(current_meals))
                    current_meals = []
    return elves


def main():
    elves = parse_input("inputs/day1.txt")
    elves = sorted(elves, reverse=True)

    print(len([e.total_calories for e in elves[:3]]))
    print(sum([e.total_calories for e in elves[:3]]))


if __name__ == "__main__":
    main()
