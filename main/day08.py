from math import lcm
from collections import defaultdict

def parse_input():
    with open("input/day08.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(filter(lambda x: x, data))

        steps = data[0]
        nodes = defaultdict(list)
        for node in data[1:]:
            node_name, directions = node.split(" = ")
            parenthesis = ["(", ")"]
            for p in parenthesis:
                directions = directions.replace(p, "")
            left_node, right_node = directions.split(", ")
            nodes[node_name].append(left_node)
            nodes[node_name].append(right_node)

    return steps, nodes

def part_one():
    steps, locs = parse_input()

    steps = list(steps) 
    steps = steps * len(locs)
    
    last_node = ""
    total_steps = 0
    current_location = locs["AAA"]
    for idx, step in enumerate(steps, start=1):
        left, right = current_location
        match step:
            case "L":
                last_node = left
            case "R":
                last_node = right
        current_location = locs[last_node]
        if last_node == "ZZZ":
            total_steps = idx
            break

    return total_steps

def part_two():
    steps, locs = parse_input()

    steps = list(steps)
    steps = steps * len(locs)

    initial_nodes = list()
    for key in locs.keys():
        if key.endswith("A"):
            initial_nodes.append(key)

    last_node = ""
    total_steps = list()
    for node in initial_nodes:
        current_location = locs[node]
        for idx, step in enumerate(steps, start=1):
            left, right = current_location
            match step:
                case "L":
                    last_node = left
                case "R":
                    last_node = right
            current_location = locs[last_node]
            if last_node.endswith("Z"):
                total_steps.append(idx)
                break

    total_steps = lcm(*total_steps)

    return total_steps

if __name__ == "__main__":
    print(part_one())
    print(part_two())
