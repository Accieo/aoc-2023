from math import prod, sqrt, ceil

def parse_input():
    with open("input/day06.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))

        races_data = list()
        for line in data:
            _, values = line.split(":")
            values = filter(lambda x: x, values.strip().split(" "))
            values = list(map(int, values))
            races_data.append(values)

        times, distances = races_data

    return times, distances

def part_one():
    times, rec_distances = parse_input()

    winning_distances = [[] for _ in range(len(times))]
    for idx, (time, record) in enumerate(zip(times, rec_distances)):
        for ms in range(1, time):
            distance = (time - ms) * ms
            if distance > record:
                winning_distances[idx].append(distance)

    ways_to_win = prod([len(race) for race in winning_distances])

    return ways_to_win

def part_two():
    times, rec_distances = parse_input()

    times = list(map(str, times))
    rec_distances = list(map(str, rec_distances))
    time = int(''.join(times))
    rec_distance = int(''.join(rec_distances))

    # Derive quadratic equation from: distance = (time - ms) * ms
    min_time = ceil((time + sqrt(time ** 2 - 4*(rec_distance))) / -2)
    max_time = ceil((time - sqrt(time ** 2 - 4*(rec_distance))) / -2)

    ways_to_win = max_time - min_time

    return ways_to_win
    
if __name__ == "__main__":
    print(part_one())
    print(part_two())
