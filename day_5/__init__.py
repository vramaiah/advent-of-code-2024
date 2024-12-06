"""Solutions for Day 5"""
import re

class OrderRule:
    
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    def __call__(self, arg: list) -> bool:
        """Checks if the given list follows the page order rule"""
        if (self.x in arg) and (self.y in arg):
            return arg.index(self.x) < arg.index(self.y)
        else:
            return True

def parse(puzzle_input: str) -> tuple:
    puzzle_input = puzzle_input.split("\n\n")
    order_rules = re.findall(r"(\d+)\|(\d+)", puzzle_input[0])
    order_rules_classes = []
    for rule in order_rules:
        x, y = rule
        order_rules_classes.append(OrderRule(int(x), int(y)))
    raw_updates = puzzle_input[1].split("\n")
    updates = []
    for update in raw_updates:
        update = update.split(",")
        updates.append([int(i) for i in update])
    return (order_rules_classes, updates)

def solve_part_1(puzzle_input):
    rules, updates = parse(puzzle_input)
    sum_middle = 0
    for update in updates:
        correct = True
        for rule in rules:
            if not rule(update):
                correct = False
                break
        if correct:
            index = len(update) // 2
            sum_middle += update[index]
    return sum_middle

def solve_part_2(puzzle_input):
    pass
