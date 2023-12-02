from math import prod
from dataclasses import dataclass

@dataclass
class GameSet:
    R: int = 0
    G: int = 0
    B: int = 0

def parse_input():
    with open("input/day02.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))
        games = dict()
        for line in data:
            game_id = line.split(":")[0].split(" ")[1]
            game_sets = list()
            for subset in line.split(": ")[1].split("; "):
                subset_cubes = subset.split(", ")
                game_set = GameSet()
                for cube in subset_cubes:
                    amount, color = cube.split(" ")
                    match color:
                        case "red":
                            game_set.R += int(amount)
                        case "green":
                            game_set.G += int(amount)
                        case "blue":
                            game_set.B += int(amount)
                game_sets.append(game_set)
            games[game_id] = game_sets

    return games

def part_one():
    games = parse_input()
    limit = GameSet(R=12, G=13, B=14)

    possible = list()
    for game, sets in games.items():
        possible_count = 0
        for subset in sets:
            if subset.R <= limit.R and subset.G <= limit.G and subset.B <= limit.B:
                possible_count += 1
            else:
                continue

        if possible_count == len(sets):
            possible.append(int(game))

    sum_of_possible = sum(possible)

    return sum_of_possible

def part_two():
    games = parse_input()

    powers = list()
    for sets in games.values():
        min_r = max([gameset.R for gameset in sets if gameset.R != 0])
        min_g = max([gameset.G for gameset in sets if gameset.G != 0])
        min_b = max([gameset.B for gameset in sets if gameset.B != 0])
        powers.append(prod([min_r, min_g, min_b]))
    
    sum_of_powers = sum(powers)

    return sum_of_powers

if __name__ == "__main__":
    print(part_one())
    print(part_two())
