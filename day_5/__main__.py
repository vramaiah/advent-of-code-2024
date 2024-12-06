import sys
import pathlib

from . import solve_part_1, solve_part_2

if __name__ == "__main__":
    paths = sys.argv[1:]
    if len(paths) == 0:
        paths.append("inputs/day_5.txt")
    for path in paths:
        puzzle_input = pathlib.Path(path).read_text().strip()
        print("====")
        print(path)
        print(f"Part 1: {solve_part_1(puzzle_input)}")
        print(f"Part 2: {solve_part_2(puzzle_input)}")
