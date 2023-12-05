def parse_input():
    with open("input/day05.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))
        mappings = dict()

        seeds = list(map(int, data[0].split(":")[1].strip().split(" ")))

        last_mapping = ""
        for line in data[2:]:
            if ":" in line:
                last_mapping = line.split(":")[0].split(" map")[0]
                mappings[last_mapping] = list()
            else:
                if line:
                    dst, src, length = list(map(int, line.split(" ")))
                    mappings[last_mapping].append([dst, src, length])

    return seeds, mappings

def part_one():
    seeds, mappings = parse_input()

    for mapping_data in mappings.values():
        current_seeds = list()
        for seed in seeds:
            found_in_range = False
            for dst, src, range_length in mapping_data:
                if seed in range(src, src + range_length):
                    current_seeds.append(seed - src + dst)
                    found_in_range = True
                    break

            if not found_in_range:
                current_seeds.append(seed)

        seeds = current_seeds

    lowest_location = min(seeds)

    return lowest_location

def part_two():
    seeds, mappings = parse_input()

    # Elves are gonna starve for now

if __name__ == "__main__":
    print(part_one())
    print(part_two())
