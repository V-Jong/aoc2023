def do_challenge():
    do_challenge_b()


class Card:
    def __init__(self, number, winning, pulled):
        self.number = number
        self.winning = winning
        self.pulled = pulled

    def __str__(self):
        return f'Number: {self.number}'

    def __repr__(self):
        return f'Number: {self.number}'


def do_challenge_a():
    file = open('4/test.txt', 'r')
    lines = file.readlines()

    total_points = 0
    with open("4/output.txt", "a") as f:
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')
            card_info = line.split(':')
            numbers = card_info[1].split('|')
            winning_numbers = [int(i) for i in numbers[0].strip().split()]
            pulled_numbers = [int(i) for i in numbers[1].strip().split()]
            common_numbers = intersection(winning_numbers, pulled_numbers)

            points = 0
            count_common = len(common_numbers)
            print(f'Common numbers: {common_numbers} ({count_common})')
            if count_common > 0:
                points = 2 ** (count_common - 1)
            print(f'Line has winning {winning_numbers} and pulled {pulled_numbers}, points: {points}\n')
            total_points += points

        print(f'Total points: {total_points}')


def do_challenge_b():
    file = open('4/input.txt', 'r')
    lines = file.readlines()

    cards = []
    count = 0
    with open("4/output.txt", "a") as f:
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')
            card_info = line.split(':')
            numbers = card_info[1].split('|')
            winning_numbers = [int(i) for i in numbers[0].strip().split()]
            pulled_numbers = [int(i) for i in numbers[1].strip().split()]
            cards.append(Card(line_index + 1, winning_numbers, pulled_numbers))

        count = count_cards(cards, cards, 0)
        print(f'Total count: {count}')


def count_cards(card_list: list[Card], original_cards: list[Card], card_index: int):
    spaces = '-' * card_index
    print(f'{spaces}Start new iteration for: {len(card_list)} cards: {card_list}')
    list_size = len(card_list)
    if list_size == 0:
        return 0
    count = list_size
    for card in card_list:
        count_common = len(intersection(card.winning, card.pulled))
        print(f'{spaces}Checking card {card}, common: {count_common}')
        start_copy = card.number
        stop_copy = start_copy + count_common
        copy_cards = original_cards[start_copy:stop_copy]
        if len(copy_cards) > 0:
            print(f'{spaces}Counting copies for {card.number}: {copy_cards}')
            count += count_cards(copy_cards, original_cards, card_index + 1)
    print(f'{spaces}Returning count for {card_index}: {count}\n')
    return count


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
