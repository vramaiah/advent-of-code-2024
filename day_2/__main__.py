import sys

from . import solve_part_1, solve_part_2

if __name__ == "__main__":
    paths = sys.argv[1:]
    if len(paths) == 0:
        paths.append("inputs/day_2.txt")
    for path in paths:
        print("====")
        print(path)
        print(f"Part 1: {solve_part_1(path)}")
        print(f"Part 2: {solve_part_2(path)}")
