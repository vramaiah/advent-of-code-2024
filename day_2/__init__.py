"""The Solutions for Day 2 of Advent of Code"""

class Report(list):
    """Class to represent a report"""
   
    @property
    def differences_list(self):
        diffs = []
        for i in range(1, len(self)):
            diffs.append(self[i] - self[i-1])
        return diffs

def parse_input(path: str):
    reports = []
    with open(path) as file:
        for line in file:
            line = line.strip().split()
            line = [int(n) for n in line]
            reports.append(Report(line))
    return reports

def solve_part_1(path: str):
    reports = parse_input(path)
    number_safe = 0
    for report in reports:
        diffs = report.differences_list
        # Amount increasing/Decreasing between 1 and 3 check
        previous_diff = None
        safe = True
        for diff in diffs:
            if not ((abs(diff) >= 1) and (abs(diff) <= 3)):
                safe = False
                break
        # All Changing check
        for diff in diffs:
            if diff == 0:
                safe = False
                break
        # All increasing / Decreasing Check
        increasing = False
        if diffs[0] > 0:
            increasing = True
        if increasing:
            for diff in diffs:
                if diff < 0:
                    safe = False
                    break
        else:
            for diff in diffs:
                if diff > 0:
                    safe = False
                    break
        if safe:
            number_safe += 1

    return number_safe

def solve_part_2(path: str):
    pass


