import threading

directions = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}

grid = {

}

passed_nodes = {

}

iter_count = 0

file = open('16/test.txt', 'r')
lines = file.read().splitlines()


def do_challenge():
    thread = threading.Thread(target=do_challenge_inner())
    thread.start()


def do_challenge_inner():
    max_x = 0
    max_y = len(lines)
    for l_index, line in enumerate(lines):
        if max_x == 0:
            max_x = len(line)
        for c_index, c in enumerate(line):
            # print(f'Adding char {c} to ({c_index},{l_index})')
            grid.update({(c_index, l_index): c})

    open('16/debug.txt', 'w').close()
    count_energized((0, 0), 'right', max_x, max_y)

    # write_to_output()
    count_list = []
    edge_nodes = [key for key, char in grid.items() if key[0] == 0 or key[0] == max_x - 1 or key[1] == 0 or key[1] == max_y - 1]
    edge_nodes_count = len(edge_nodes) + 4
    print(f'Checking energized for {edge_nodes_count} nodes')
    count_done = 0
    for key in edge_nodes:
        global passed_nodes
        x = key[0]
        y = key[1]
        if x == 0:
            passed_nodes = {}
            count_energized(key, 'right', max_x, max_y)
            count_list.append(count_checked())
            count_done += 1
        if x == max_x - 1:
            passed_nodes = {}
            count_energized(key, 'left', max_x, max_y)
            count_list.append(count_checked())
            count_done += 1
        if y == 0:
            passed_nodes = {}
            count_energized(key, 'down', max_x, max_y)
            count_list.append(count_checked())
            count_done += 1
        if y == max_y - 1:
            passed_nodes = {}
            count_energized(key, 'up', max_x, max_y)
            count_list.append(count_checked())
            count_done += 1
        print(f'{count_done / edge_nodes_count * 100}% done')

    print(f'Calculated energized: {count_list}')
    print(f'Max: {max(count_list)}')


def count_energized(current_node: (int, int), direction: str, max_x: int, max_y: int):
    stack = [(current_node, direction, 0)]  # (node, direction, counter)

    with open("16/debug.txt", "a") as f:
        while stack:
            current_node, direction, counter = stack.pop()

            print(
                f'\nChecking {current_node} while going {direction}, current count {counter} with max x {max_x} and max y {max_y}',
                file=f)
            f.flush()
            if (current_node[0] < 0 or current_node[0] >= max_x) or (current_node[1] < 0 or current_node[1] >= max_y):
                print(f'Stopping since {current_node} in out of bounds, returning {counter}', file=f)
                f.flush()
                continue
            if any(pn for pn in passed_nodes if pn[0] == current_node[0] and pn[1] == current_node[1] and pn[2] == direction):
                char = grid.get(current_node)
                passed_count = passed_nodes.get((current_node[0], current_node[1], direction))
                if passed_count == 1 and char == '.':
                    print(f'Stopping {char} since {current_node} in cache, returning {counter}', file=f)
                    f.flush()
                    continue
                if passed_count == 1 and (char == '\\' or char == '/'):
                    print(f'Stopping {char} since {current_node} in cache, returning {counter}', file=f)
                    f.flush()
                    continue
                if passed_count == 1 and (char == '-' or char == '|'):
                    print(f'Stopping {char} since {current_node} in cache, returning {counter}', file=f)
                    f.flush()
                    continue
                if passed_count == 0:
                    print(f'Passed count: {passed_count} for {current_node}, updating + 1', file=f)
                    f.flush()
                    passed_nodes.update({(current_node[0], current_node[1], direction): passed_count + 1})
                    print(f'New passed count: {passed_nodes.get((current_node[0], current_node[1], direction))}', file=f)
                    f.flush()
            if not any(pn for pn in passed_nodes if pn[0] == current_node[0] and pn[1] == current_node[1]):
                print(f'Not encountered {current_node} with direction {direction}, adding to cache', file=f)
                passed_nodes.update({(current_node[0], current_node[1], direction): 1})
                counter += 1
            current_char = grid.get(current_node)
            print(f'Character at {current_node} is {current_char}', file=f)
            f.flush()

            if current_char == '.':
                next_direction = directions.get(direction)
                next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                print(f'Going {direction} to {next_node}', file=f)
                f.flush()
                stack.append((next_node, direction, counter))
            elif current_char == "\\":
                new_direction = ''
                if direction == 'right':
                    new_direction = 'down'
                if direction == 'up':
                    new_direction = 'left'
                if direction == 'left':
                    new_direction = 'up'
                if direction == 'down':
                    new_direction = 'right'
                next_direction = directions.get(new_direction)
                next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                print(f'Going {new_direction} to {next_node}', file=f)
                f.flush()
                stack.append((next_node, new_direction, counter))
            elif current_char == '/':
                new_direction = ''
                if direction == 'right':
                    new_direction = 'up'
                if direction == 'up':
                    new_direction = 'right'
                if direction == 'left':
                    new_direction = 'down'
                if direction == 'down':
                    new_direction = 'left'
                next_direction = directions.get(new_direction)
                next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                print(f'Going {new_direction} to {next_node}', file=f)
                f.flush()
                stack.append((next_node, new_direction, counter))
            elif current_char == '-':
                if direction == 'right' or direction == 'left':
                    next_direction = directions.get(direction)
                    next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                    print(f'Going {direction} to {next_node}', file=f)
                    f.flush()
                    stack.append((next_node, direction, counter))
                if direction == 'up' or direction == 'down':
                    left_node = (current_node[0] - 1, current_node[1])
                    right_node = (current_node[0] + 1, current_node[1])
                    stack.append((left_node, 'left', counter))
                    stack.append((right_node, 'right', counter))
            elif current_char == '|':
                if direction == 'right' or direction == 'left':
                    up_node = (current_node[0], current_node[1] - 1)
                    down_node = (current_node[0], current_node[1] + 1)
                    stack.append((up_node, 'up', counter))
                    stack.append((down_node, 'down', counter))
                elif direction == 'up' or direction == 'down':
                    next_direction = directions.get(direction)
                    next_node = (current_node[0] + next_direction[0], current_node[1] + next_direction[1])
                    print(f'Going {direction} to {next_node}', file=f)
                    f.flush()
                    stack.append((next_node, direction, counter))


def count_checked():
    count_checks = 0
    for node in passed_nodes:
        count_checks += 1
    return count_checks


def write_to_output():
    open('16/output.txt', 'w').close()
    # clear()
    with open("16/output.txt", "a") as f:
        for l_index, line in enumerate(lines):
            n_line = ''
            for c_index, c in enumerate(line):
                if any(pn for pn in passed_nodes if pn[0] == c_index and pn[1] == l_index):
                    n_line += '#'
                else:
                    n_line += '.'
            print(f'{n_line}', file=f)
        print('')
