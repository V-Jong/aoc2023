import re


class Number:
    def __init__(self, number, start, end, line_index):
        self.number = number
        self.start = start
        self.end = end
        self.line_index = line_index

    def is_left_or_right(self, symbol_position):
        return self.start - 1 == symbol_position or self.end + 1 == symbol_position

    def is_top_or_bottom(self, symbol_position, symbol, f):
        print(
            f'Checking if symbol {symbol} at position {symbol_position} is top or bottom {self.start} and {self.end} for number {self.number}: {self.start <= symbol_position <= self.end}',
            file=f)
        return self.start <= symbol_position <= self.end

    def is_diagonal(self, symbol_position, symbol, f):
        diagonal_threshold = 1
        left_diagonal = symbol_position - diagonal_threshold
        right_diagonal = symbol_position + diagonal_threshold
        print(
            f'Checking if symbol {symbol} at position {symbol_position} with left diagonal {left_diagonal} or right diagonal '
            f'{right_diagonal} is between {self.start} and {self.end} for number {self.number}: '
            f'{self.start <= left_diagonal <= self.end} or {self.start <= right_diagonal <= self.end}', file=f)
        return self.start <= left_diagonal <= self.end or self.start <= right_diagonal <= self.end

    def __str__(self):
        return f'Number: {self.number} and position: ({self.start}, {self.end}), line: {self.line_index}'

    def __repr__(self):
        return f'Number: {self.number} and position: ({self.start}, {self.end}), line: {self.line_index}'


class Symbol:
    def __init__(self, character, position, line_index):
        self.character = character
        self.position = position
        self.line_index = line_index

    def __str__(self):
        return f'Symbol: {self.character} and position: ({self.position}), line: {self.line_index}'

    def __repr__(self):
        return f'Symbol: {self.character} and position: ({self.position}), line: {self.line_index}'


def do_challenge():
    do_challenge_b()


def do_challenge_a():
    file = open('3/input.txt', 'r')
    lines = file.readlines()

    numbers = []
    symbols = []
    with open("3/output.txt", "a") as f:
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')
            # print(f'Processing line ({line_index}): {line}')

            line_numbers = re.findall(r'\d+', line)
            # for line_number in line_numbers:
            #     key_indexes = [m.start() for m in re.finditer(line_number, line)]  # line.find(key)
            #     print(f'Indexes for {line_number}: {key_indexes} on line {line_index}')
            #     if len(key_indexes) > 0:
            #         for key_index in key_indexes:
            #             if not any(n for n in numbers if n.number == int(line_number) and n.line_index == line_index and n.start == key_index and n.end == key_index + len(line_number) - 1):
            #                 numbers.append(Number(int(line_number), key_index, key_index + len(line_number) - 1, line_index))
            line_numbers = [Number(int(m.group(0)), m.start(0), m.end() - 1, line_index) for m in re.finditer(r'\d+', line)]
            for line_number in line_numbers:
                numbers.append(line_number)

            line_chars = [*line]
            for index, line_char in enumerate(line_chars):
                # print(f'Symbol found: {line_char}')
                if not line_char.isalnum() and line_char != '.':
                    if not any(n for n in symbols if
                               n.character == line_char and n.line_index == line_index and n.position == index):
                        symbols.append(Symbol(line_char, index, line_index))

        # print(f'Numbers found: {numbers}')
        for numberx in numbers:
            print(f'Number found {numberx}')
        # print(f'Symbols found: {symbols}')
        print(f'Symbols found: {set(map(lambda s: s.character, symbols))}\n', file=f)

        numbers_sum = []
        for number in numbers:
            print(
                f'Processing number {number.number} at line {number.line_index}, start {number.start}, end {number.end}',
                file=f)
            current_line_index = number.line_index
            next_line_index = number.line_index + 1

            # Check if number has any symbols in current line which are left or right
            # symbol_position = number.position
            current_line_symbols = get_symbols_for_line(symbols, current_line_index)
            for current_line_symbol in current_line_symbols:
                # print(f'Checking if symbol {symbol.character} at position {symbol_position} is adjacent to {current_line_number}')
                if number.is_left_or_right(current_line_symbol.position):
                    print(
                        f'Number {number.number} has symbol {current_line_symbol.character} left or right in line {current_line_index}',
                        file=f)
                    add_numbers_sum(numbers_sum, number, f)

            # Check if number has any symbols in previous line which are top or bottom or diagonal
            if current_line_index >= 1:
                prev_line_index = current_line_index - 1
                prev_line_symbols = get_symbols_for_line(symbols, prev_line_index)
                for prev_line_symbol in prev_line_symbols:
                    if number.is_top_or_bottom(prev_line_symbol.position, prev_line_symbol.character,
                                               f) or number.is_diagonal(prev_line_symbol.position,
                                                                        prev_line_symbol.character, f):
                        print(
                            f'Number {number.number} has symbol {prev_line_symbol.character} top or bottom or diagonal in prev line {prev_line_index}',
                            file=f)
                        add_numbers_sum(numbers_sum, number, f)

            # Check if number has any symbols in next line which are top or bottom or diagonal
            next_line_symbols = get_symbols_for_line(symbols, next_line_index)
            for next_line_symbol in next_line_symbols:
                if number.is_top_or_bottom(next_line_symbol.position, next_line_symbol.character,
                                           f) or number.is_diagonal(next_line_symbol.position,
                                                                    next_line_symbol.character, f):
                    print(
                        f'Number {number.number} has symbol {next_line_symbol.character} top or bottom or diagonal in next line {next_line_index}',
                        file=f)
                    add_numbers_sum(numbers_sum, number, f)
            # print('')

        # numbers_sum.sort(key=lambda s: s.line_index)
        # print(f'Numbers to sum:')
        # for number_sum in numbers_sum:
        #     print(f'{number_sum}')
        final_sum = sum(list(map(lambda s: s.number, numbers_sum)))
        print(f'Final sum: {final_sum}')


def do_challenge_b():
    file = open('3/input.txt', 'r')
    lines = file.readlines()

    numbers = []
    symbols = []
    with (open("3/output.txt", "a") as f):
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')

            line_numbers = [Number(int(m.group(0)), m.start(0), m.end() - 1, line_index) for m in
                            re.finditer(r'\d+', line)]
            for line_number in line_numbers:
                numbers.append(line_number)

            line_chars = [*line]
            for index, line_char in enumerate(line_chars):
                # print(f'Evaluating char {line_char}')
                if line_char == '*':
                    if not any(n for n in symbols if n.character == line_char and n.line_index == line_index and n.position == index):
                        # print(f'Adding char {line_char}')
                        symbols.append(Symbol(line_char, index, line_index))

        number_sum = 0
        for symbol in symbols:
            # print(f'Symbol found: {symbol}')
            current_line_index = symbol.line_index
            next_line_index = symbol.line_index + 1
            gear_numbers = []

            # Check if number has any symbols in current line which are left or right
            symbol_position = symbol.position
            current_line_numbers = get_numbers_for_line(numbers, current_line_index)
            for current_line_number in current_line_numbers:
                # print(f'Checking if symbol {symbol.character} at position {symbol_position} is adjacent to {current_line_number}')
                if current_line_number.is_left_or_right(symbol_position):
                    print(
                        f'Number {current_line_number.number} has symbol {symbol.character} left or right in line {current_line_index}',
                        file=f)
                    gear_numbers.append(current_line_number)

            # Check if number has any symbols in previous line which are top or bottom or diagonal
            if current_line_index >= 1:
                prev_line_index = current_line_index - 1
                prev_line_numbers = get_numbers_for_line(numbers, prev_line_index)
                for prev_line_number in prev_line_numbers:
                    if prev_line_number.is_top_or_bottom(symbol_position, symbol.character, f) or prev_line_number.is_diagonal(symbol.position, symbol.character, f):
                        print(
                            f'Number {prev_line_number.number} has symbol {symbol.character} top or bottom or diagonal in prev line {prev_line_index}',
                            file=f)
                        gear_numbers.append(prev_line_number)

            # Check if number has any symbols in next line which are top or bottom or diagonal
            next_line_numbers = get_numbers_for_line(numbers, next_line_index)
            for next_line_number in next_line_numbers:
                if next_line_number.is_top_or_bottom(symbol.position, symbol.character, f) or next_line_number.is_diagonal(symbol.position, symbol.character, f):
                    print(
                        f'Number {next_line_number.number} has symbol {symbol.character} top or bottom or diagonal in next line {next_line_index}',
                        file=f)
                    gear_numbers.append(next_line_number)

            if len(gear_numbers) == 2:
                print(f'Symbol {symbol} has 2 gear numbers {gear_numbers}')
                power_gear = gear_numbers[0].number * gear_numbers[1].number
                print(f'Power is {power_gear}')
                number_sum += power_gear
        print(f'Number sum {number_sum}')


def get_numbers_for_line(numbers: list[Number], line_index: int):
    return [x for x in numbers if x.line_index == line_index]


def get_symbols_for_line(symbols: list[Symbol], line_index: int):
    return [x for x in symbols if x.line_index == line_index]


def add_numbers_sum(numbers: list[Number], number: Number, f):
    if not any(n for n in numbers if
               n.number == number.number and n.line_index == number.line_index and n.start == number.start and n.end == number.end):
        numbers.append(number)
    else:
        print(f'Skipping adding existing number {number}', file=f)
