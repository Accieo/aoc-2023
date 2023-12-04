def parse_input():
    with open("input/day04.txt", "r") as file:
        data = file.readlines()
        data = list(map(str.strip, data))

        win, own = list(), list()
        for line in data:
            entry = line.split(": ")[1]
            winning_nums, own_nums = entry.split(" | ")
            winning_nums = winning_nums.split(" ")
            winning_nums = list(filter(lambda x: x != "", winning_nums))
            winning_nums = list(map(int, winning_nums))
            win.append(winning_nums)
            own_nums = own_nums.split(" ")
            own_nums = list(filter(lambda x: x != "", own_nums))
            own_nums = list(map(int, own_nums))
            own.append(own_nums)

    return win, own

def part_one():
    win, own = parse_input()

    total_score = 0
    for own_nums, win_nums in zip(own, win):
        score = 0
        for entry in own_nums:
            if entry in win_nums:
                if score == 0:
                    score += 1
                else:
                    score += score
        total_score += score

    return total_score

def part_two():
    win, own = parse_input()

    deck_of_cards = {k: 1 for k in range(0, len(win))}

    for card_num, (own_nums, win_nums) in enumerate(zip(own, win)):
        matching_cards = 0
        for entry in own_nums:
            if entry in win_nums:
                matching_cards += 1
        for i in range(card_num + 1, card_num + matching_cards + 1):
            deck_of_cards[i] += deck_of_cards[card_num]

    total_scratchcards = sum(deck_of_cards.values())

    return total_scratchcards

if __name__ == "__main__":
    print(part_one())
    print(part_two())
