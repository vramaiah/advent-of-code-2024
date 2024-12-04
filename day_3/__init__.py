"""The solutions for day 3 of Advent of Code"""

import re

def solve_part_1(puzzle_input: str) -> int:
    matches = re.findall(r"mul\((\d+),(\d+)\)", puzzle_input)
    sum = 0
    for x, y in matches:
        sum += int(x) * int(y)
    return sum

def solve_part_2(puzzle_input: str):
    instructions_regex = r"mul\(\d+,\d+\)" + "|" + r"don't\(\)" + "|" + r"do\(\)"
    multiplication_regex = r"mul\((\d+),(\d+)\)"
    instructions = re.findall(instructions_regex, puzzle_input)
    multiplication_on = True
    sum = 0
    for instruction in instructions:
        if instruction == "don't()":
            multiplication_on = False
        if instruction == "do()":
            multiplication_on = True
        if re.fullmatch(multiplication_regex, instruction) and multiplication_on:
            n = re.findall(multiplication_regex, instruction)
            x,y = n[0]
            sum += int(x) * int(y)
    return sum
