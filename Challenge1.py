import re

number_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


class Countable:
    def __init__(self, index, number):
        self.index = index
        self.number = number

    def __str__(self):
        return f'Index: {self.index} and value: {self.number}'

    def __repr__(self):
        return f'Index: {self.index} and value: {self.number}'


def do_challenge():
    file = open('1/input.txt', 'r')
    lines = file.readlines()
    numbers = []
    for line in lines:
        line = line.replace('\n', '')
        line_numbers = []
        for key, value in number_map.items():
            key_indexes = [m.start() for m in re.finditer(key, line)]  # line.find(key)
            # print(f'Indexes for {key}: {key_indexes}')
            if len(key_indexes) > 0:
                for key_index in key_indexes:
                    # print(f'Found {key} at index {key_index}')
                    line_numbers.append(Countable(key_index, value))
        line_chars = [*line]
        print(f'Original line is {line}')  # , updated is {updated_line}')
        for index, line_char in enumerate(line_chars):
            if line_char.isnumeric():
                line_numbers.append(Countable(index, int(line_char)))
        # line_numbers = re.findall(r'\d+', line)
        if len(line_numbers) > 0:
            line_numbers.sort(key=lambda x: x.index)
            line_numbers = [o.number for o in line_numbers]
            print(f'Found all numbers: {line_numbers}')
            first_number = line_numbers[0]
            last_number = line_numbers[len(line_numbers) - 1]
            final_number = str(first_number) + str(last_number)
            print(f'Numbers {line_numbers}, first {first_number}, last {last_number}, final {final_number}\n')
            numbers.append(int(final_number))
    sum_numbers = sum(numbers)
    print(f'Sum: {sum_numbers}')
