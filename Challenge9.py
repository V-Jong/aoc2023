import re


def do_challenge():
    file = open('9/input.txt', 'r')
    lines = file.readlines()
    next_numbers = []
    for line in lines:
        line_numbers = [int(d) for d in re.findall(r'-?\d+', line)]
        line_numbers.reverse()

        next_number = find_steps_until_zero(line_numbers, line_numbers[-1])
        print(f'Next step is: {next_number}')
        print()
        next_numbers.append(next_number)
    print(f'Sum: {sum(next_numbers)}')


def find_steps_until_zero(numbers: list[int], previous_last_step: int):
    if all(n == 0 for n in numbers):
        return previous_last_step
    steps = []
    for index, number in enumerate(numbers):
        if index < len(numbers) - 1:
            # print(f'Checking number {number} at index {index}')
            step = numbers[index + 1] - number
            steps.append(step)
    print(f'Numbers are {numbers}')
    print(f'Steps are     {steps}')
    print(f'Previous last step: {previous_last_step}')
    if len(set(steps)) == 1 and steps[0] == 0:
        return previous_last_step
    else:
        return previous_last_step + find_steps_until_zero(steps, steps[-1])
