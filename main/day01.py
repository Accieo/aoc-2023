def parse_input():
    with open("input/day01.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))

    return data

def part_one():
    calibration_document = parse_input()
    calibration_values = list()

    for line in calibration_document:
        first, last = "", ""
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in reversed(line):
            if char.isdigit():
                last = char
                break

        calibration_values.append(int(first + last))

    calibration_values_sum = sum(calibration_values)

    return calibration_values_sum

def part_two():
    calibration_document = parse_input()
    calibration_values = list()
    table = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in calibration_document:
        ordered_occurrences = dict()
        for k in table.keys():
            spelled_idxs = [i for i in range(len(line)) if line.startswith(k, i)]
            for idx in spelled_idxs:
                ordered_occurrences[idx] = table[k]
        for char in line:
            if char.isdigit():
                idx = line.find(char)
                if idx != -1:
                    ordered_occurrences[idx] = char
        for char in line:
            if char.isdigit():
                idx = line.rfind(char)
                if idx != 1:
                    ordered_occurrences[idx] = char
        ordered_occurrences = dict(sorted(ordered_occurrences.items()))

        list_ordered_occurrences = list(ordered_occurrences.items())
        first = list_ordered_occurrences[0][1]
        last = list_ordered_occurrences[-1][1]
        calibration_values.append(int(first + last))

    calibration_values_sum = sum(calibration_values)

    return calibration_values_sum

if __name__ == "__main__":
    print(part_one())
    print(part_two())
