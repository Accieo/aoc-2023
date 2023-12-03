from string import punctuation
from math import prod

def parse_input():
    with open("input/day03.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))

    return data

def get_neighbors(x: int, y: int, max_length: int) -> list[tuple[int, int]]:
    # diffs = [down, up, left, right, down-right, up-right, down-left, up-left]
    diffs = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = list(map(lambda diff: (x + diff[0], y + diff[1]), diffs))
    neighbors = list(filter(lambda coord: (0 <= coord[0] < max_length) and (0 <= coord[1] < max_length), neighbors))

    return neighbors

def part_one():
    engine_schematic = parse_input()
    max_length = len(engine_schematic[0])
    punctuation_no_dot = punctuation.replace(".", "")

    part_numbers = list()
    for idxy, line in enumerate(engine_schematic):
        digit = ""
        has_adjacent_symbol = False
        for idxx, char in enumerate(line):
            right = engine_schematic[idxy][idxx + 1] if idxx + 1 < max_length else ""
            if char.isdigit():
                for x, y in get_neighbors(x=idxx, y=idxy, max_length=max_length):
                    if engine_schematic[y][x] in punctuation_no_dot:
                        has_adjacent_symbol = True
                digit += char
                if has_adjacent_symbol and right in punctuation:
                    part_numbers.append(int(digit))
            else:
                has_adjacent_symbol = False
                digit = ""

    sum_of_part_numbers = sum(part_numbers)
    
    return sum_of_part_numbers

def part_two():
    engine_schematic = parse_input()
    max_length = len(engine_schematic[0])

    gears = dict()
    for idxy, line in enumerate(engine_schematic):
        digit = ""
        latest_gear = ""
        has_adjacent_gear = False
        for idxx, char in enumerate(line):
            right = engine_schematic[idxy][idxx + 1] if idxx + 1 < max_length else ""
            if char.isdigit():
                for x, y in get_neighbors(x=idxx, y=idxy, max_length=max_length):
                    if engine_schematic[y][x] == "*":
                        if f"{y}-{x}" not in gears.keys():
                            gears[f"{y}-{x}"] = list()
                        latest_gear = f"{y}-{x}"
                        has_adjacent_gear = True
                digit += char
                if has_adjacent_gear and right in punctuation:
                    gears[latest_gear].append(int(digit))
            else:
                has_adjacent_gear = False
                digit = ""

    valid_gears = {k: v for k, v in gears.items() if len(v) > 1}
    gear_ratios = list(map(lambda x: prod(x), valid_gears.values()))
    sum_of_gear_ratios = sum(gear_ratios)
    
    return sum_of_gear_ratios

if __name__ == "__main__":
    print(part_one())
    print(part_two())
