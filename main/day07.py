from typing import Literal
from collections import Counter, defaultdict

def parse_input():
    with open("input/day07.txt", "r") as file:
        data = file.read().splitlines()
        cards = defaultdict()
        for entry in data:
            card, bid = entry.split(" ")
            cards[card] = int(bid)

    return cards

def check_five(hand: str) -> bool:
    """Five cards have the same label"""
    if len(set(hand)) == 1:
        return True
    return False

def check_four(hand: str) -> bool:
    """Four cards have the same label"""
    if len(set(hand)) == 2:
        counter = Counter(hand).most_common(1)[0][1]
        if counter == 4:
            return True
    return False

def check_full(hand: str) -> bool:
    """Three cards have the same label, two same label"""
    if len(set(hand)) == 2:
        counter = Counter(hand).most_common(1)[0][1]
        if counter == 3:
            return True
    return False

def check_three(hand: str) -> bool:
    """Three cards have the same label, rest different"""
    if len(set(hand)) == 3:
        counter = Counter(hand).most_common(1)[0][1]
        if counter == 3:
            return True
    return False

def check_tpair(hand: str) -> bool:
    """Two pairs and one single different card"""
    if len(set(hand)) == 3:
        counter = Counter(hand).most_common(2)
        first, second = counter[0][1], counter[1][1]
        if first == 2 and second == 2:
            return True
    return False

def check_opair(hand: str) -> bool:
    """One pair and three cards are all different"""
    if len(set(hand)) == 4:
        return True
    return False

def check_high(hand: str) -> bool:
    """All cards are different"""
    if len(set(hand)) == len(hand):
        return True
    return False

def check_hand(hand: str) -> int:
    """Returns rank of the given hand 1 highest -> 7 lowest"""
    if check_five(hand):
        return 1
    elif check_four(hand):
        return 2
    elif check_full(hand):
        return 3
    elif check_three(hand):
        return 4
    elif check_tpair(hand):
        return 5
    elif check_opair(hand):
        return 6
    elif check_high(hand):
        return 7
    return 0

def best_hand_type(hand: str) -> int:
    if len(set(hand)) == 1:
        if "J" in set(hand):
            return check_hand(hand="AAAAA")
    if "J" in hand:
        mc_card, _ = Counter(hand.replace("J", "")).most_common(1)[0]
        return check_hand(hand=hand.replace("J", mc_card))

    return check_hand(hand=hand)

def solve(part: Literal[1, 2] = 1) -> int:
    cards = parse_input()

    unsorted = defaultdict(list)

    values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    if part != 1:
        values["J"] = 1

    inv_values = {v: k for k, v in values.items()}
    for hand in cards.keys():
        hand_list = [values[c] if c in values.keys() else int(c) for c in hand]

        if part == 1:
            unsorted[check_hand(hand=hand)].append(hand_list)
        else:
            unsorted[best_hand_type(hand=hand)].append(hand_list)

    unsorted = dict(sorted(unsorted.items()))

    for value in unsorted.values():
        value.sort()

    by_rank = list()
    for win_type in unsorted.values():
        for hand in reversed(win_type):
            original = ''.join([inv_values[c] if c in inv_values.keys() else str(c) for c in hand])
            by_rank.append(original)

    total_winnings = sum([cards[hand] * idx for idx, hand in enumerate(reversed(by_rank), start=1)])

    return total_winnings

def part_one():
    return solve(part=1)

def part_two():
    return solve(part=2)

if __name__ == "__main__":
    print(part_one())
    print(part_two())
