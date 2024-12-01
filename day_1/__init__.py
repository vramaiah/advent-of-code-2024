"""The solution for day 1 of Advent of Code"""
def extract_lists(path: str):
    with open(path) as f:
        list_l = []
        list_r = []
        for line in f:
            line = line.strip()
            line = line.split()
            list_l.append(int(line[0]))
            list_r.append(int(line[1]))
    return (list_l, list_r)

def solve_part_1(path: str):
    (list_l, list_r) = extract_lists(path)
    list_l.sort()
    list_r.sort()
    sum_diffs = 0
    for items in zip(list_l, list_r):
        items = list(items)
        sum_diffs += abs(items[0] - items[1])
    return sum_diffs

def solve_part_2(path: str):
    (list_l, list_r) = extract_lists(path)
    similarity = 0
    for item in list_l:
        similarity += item * list_r.count(item)
    return similarity
