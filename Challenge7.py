import itertools
import re
from collections import Counter

card_strength = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10
}

hand_kinds = {
    'high-card': [],
    'one-pair': [],
    'two-pair': [],
    'three-of-kind': [],
    'full-house': [],
    'four-of-kind': [],
    'five-of-kind': []
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.rank = 0
        self.strength = -1

    def set_rank(self, rank):
        self.rank = rank

    def set_strength(self, strength):
        self.strength = strength

    def __str__(self):
        return f'Hand: {self.cards}; rank: {self.rank}; str: {self.strength}'

    def __repr__(self):
        return f'Hand: {self.cards}; rank: {self.rank}; str: {self.strength}'


def do_challenge():
    file = open('7/input.txt', 'r')
    lines = file.readlines()

    hands = []
    for line in lines:
        line = line.split()
        hands.append(Hand(line[0], int(line[1])))

    determine_hand_kinds(hands)
    # print(f'five of a kind {hand_kinds.get("five-of-kind")}')
    set_hand_ranks(hand_kinds)
    # print(f'After rank: {hands}')
    for hand in hands:
        print(f'Hand {hand}')
    print(f'Multiplying: {list(map(lambda h: str(h.bid) + " * " + str(h.rank), hands))}')
    multiples = list(map(lambda h: h.rank * h.bid, hands))
    print(f'Multiples: {multiples}')
    print(f'Final: {sum(multiples)}')


def determine_hand_kinds(hands: list[Hand]):
    for hand in hands:
        counter = Counter(hand.cards)
        most_commons = counter.most_common(2)
        # print(f'{hand.cards}, commons: {most_commons}')
        most_common = most_commons[0]
        if most_common[1] == 5:
            hand_kinds['five-of-kind'].append(hand)
        else:
            second_most_common = most_commons[1]
            # print(f'Most common {most_common}, second {second_most_common}')

            joker_count = len(re.findall('J', hand.cards))
            if joker_count == most_common[1]:
                set_group_for_hand(second_most_common[1] + joker_count, second_most_common[1], hand)
            else:
                set_group_for_hand(most_common[1] + joker_count, second_most_common[1], hand)


def set_group_for_hand(most_common_count: int, second_most_common_count: int, hand: Hand):
    if most_common_count == 5:
        hand_kinds['five-of-kind'].append(hand)
    if most_common_count == 4:
        hand_kinds['four-of-kind'].append(hand)
    if most_common_count == 3:
        if second_most_common_count == 2:
            hand_kinds['full-house'].append(hand)
        else:
            hand_kinds['three-of-kind'].append(hand)
    if most_common_count == 2:
        if second_most_common_count == 2:
            hand_kinds['two-pair'].append(hand)
        else:
            hand_kinds['one-pair'].append(hand)
    if most_common_count == 1:
        hand_kinds['high-card'].append(hand)


def set_hand_ranks(game: dict):
    rank = 1
    for kind, hands in filter(lambda g: len(g[1]) > 0, game.items()):
        # print(f'kind {kind}, hands {hands}')
        if len(hands) == 1:
            hands[0].set_rank(rank)
            rank += 1
        else:
            print(f'Sorting for kind {kind}')
            ordered = sort_hands(hands.copy(), [], 0)
            # ordered.sort(key=lambda x: x.strength)
            for hand in ordered:
                hand.set_rank(rank)
                rank += 1
            # print(f'Ordered hands: {ordered}\n')

        print()


def sort_hands(remaining: list[Hand], ordered: list[Hand], char_index: int):
    if len(remaining) == 0:
        return []
    mapped = list(map(lambda h: (h.cards, h), remaining))
    # print(f'Checking index {char_index} for remaining {len(remaining)} and mapped: {mapped}')
    to_evaluate = [(c[char_index], h) for (c, h) in mapped]
    card_strengths = []
    for symbol, hand in to_evaluate:
        strength = get_card_strength(symbol)
        hand.set_strength(strength)
        card_strengths.append(strength)
    # print(f'Evaluating cards: {to_evaluate}')
    remaining.sort(key=lambda c: c.strength)
    duplicates_grouped = [(k, list(g)) for k, g in itertools.groupby(remaining, lambda h: h.strength)]
    # print(f'groups: {[(k, len(g)) for k, g in duplicates_grouped]}')
    for duplicate_strength, cards in duplicates_grouped:
        if len(cards) == 1:
            remaining.remove(cards[0])
            ordered.append(cards[0])
        else:
            # print(f'Passing to next iteration {char_index + 1}: {cards}')
            sort_hands(cards, ordered, char_index + 1)
            # print(f'Returned from {char_index + 1}: {returned}')

    # print(f'Returning from {char_index}: {ordered}\n')
    # ordered.sort(key=lambda x: x.strength)
    return ordered


def get_card_strength(symbol: str):
    if symbol.isnumeric():
        return int(symbol)
    else:
        return card_strength.get(symbol)
