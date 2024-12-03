class File:
    """File"""

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Directory:
    """Directory"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.parent = None
        self.files = []
        self.total_size = 0

    def add(self, file: File) -> None:
        """add"""
        self.files.append(file)
        self.total_size += file.size
        if self.parent:
            self.parent.add(file)

    def __repr__(self) -> str:
        return f"{self.name} : {self.total_size}"

    def __str__(self) -> str:
        return f"{self.name} : {self.total_size}"

    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.total_size == other.total_size

    def __lt__(self, other: object) -> bool:
        return self.total_size < other.total_size


def main():
    with open("inputs/day7.txt", "r", encoding="utf8") as f:
        lines = [l.strip() for l in f.readlines()]

    visited_dirs = []
    dirs = []
    for line in lines:
        if line.startswith("$ cd"):
            if line[-2:] == "..":
                visited_dirs.pop()
            else:
                new_dir = Directory(line[5:])
                if visited_dirs:
                    new_dir.parent = visited_dirs[-1]
                dirs.append(new_dir)
                visited_dirs.append(new_dir)

        elif line == "$ ls" or line.startswith("dir"):
            continue
        else:
            size, name = line.split()
            new_file = File(name, int(size))
            visited_dirs[-1].add(new_file)

    # day 1
    # --------
    # total = 0
    # for dir in dirs:
    #     if dir.name != "/" and dir.total_size <= 100000:
    #         total += dir.total_size

    total_space = 70000000
    target_unused_space = 30000000
    total = dirs[0].total_size
    current_unused = total_space - total
    target = target_unused_space - current_unused

    candidates = []
    for d in dirs:
        if d.total_size >= target:
            candidates.append(d)

    candidates.sort()
    print(candidates[0])


if __name__ == "__main__":
    main()
