class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


def do_challenge():
    file = open('14/test.txt', 'r')
    lines = file.read().splitlines()

    rocks = []
    blocks = []
    x_limit = 0
    for line_index, line in enumerate(lines):
        chars = [*line]
        x_limit = len(chars)
        for c_index, char in enumerate(chars):
            if char == 'O':
                rocks.append(Rock(c_index, line_index))
            if char == '#':
                blocks.append(Block(c_index, line_index))

    max_points = len(lines)
    # move_north(rocks, blocks)
    # print(f'Blocks after moving north')
    # to do: 1000000000
    do_cycle(3, rocks, blocks, len(lines), x_limit)
    rocks.sort(key=lambda r: r.x)
    sum_points = 0
    for rock in rocks:
        print(f'{rock}, points: {max_points - rock.y}')
        sum_points += max_points - rock.y

    print(f'Sum: {sum_points}')


def do_cycle(times: int, rocks: list[Rock], blocks: list[Block], y_limit: int, x_limit: int):
    for i in range(0, times, 1):
        move_north(rocks, blocks)
        print_to_file(rocks, blocks, x_limit, y_limit)
        move_west(rocks, blocks)
        print_to_file(rocks, blocks, x_limit, y_limit)
        move_south(rocks, blocks, y_limit)
        print_to_file(rocks, blocks, x_limit, y_limit)
        move_east(rocks, blocks, x_limit)
        # print_to_file(rocks, blocks, x_limit, y_limit)
        print_to_file(rocks, blocks, x_limit, y_limit)
        with open("14/output.txt", "a") as f:
            print(f'Cycle {i} done\n', file=f)


def move_north(rocks: list[Rock], blocks: list[Block]):
    rocks.sort(key=lambda r: r.x)
    for rock in rocks:
        # print()
        blocking_blocks = [b for b in blocks if rock.y > b.y and rock.x == b.x]
        # print(f'Blocking blocks for {rock} = {blocking_blocks}')
        if len(blocking_blocks) > 0:
            max_y = 0
            for b_block in blocking_blocks:
                if b_block.y > max_y:
                    max_y = b_block.y

            blocking_rocks = [r for r in rocks if rock.y > r.y > max_y and rock.x == r.x]
            # print(f'Blocking rocks after block for {rock} = {blocking_rocks}')

            if len(blocking_rocks) > 0:
                # move to lowest rock
                max_y = 0
                for b_rock in blocking_rocks:
                    if b_rock.y > max_y:
                        max_y = b_rock.y
            # print(f'Lowest block is at y {max_y}')
            rock.y = max_y + 1
        else:
            blocking_rocks = [r for r in rocks if rock.y > r.y and rock.x == r.x]
            # print(f'Blocking rocks for {rock} = {blocking_rocks}')

            if len(blocking_rocks) == 0:
                # move to lowest y
                rock.y = 0
            else:
                # move to lowest rock
                max_y = 0
                for b_rock in blocking_rocks:
                    if b_rock.y > max_y:
                        max_y = b_rock.y
                # print(f'Lowest rock is at y {max_y}')
                rock.y = max_y + 1


def move_west(rocks: list[Rock], blocks: list[Block]):
    rocks.sort(key=lambda r: r.x)
    for rock in rocks:
        # print()
        blocking_blocks = [b for b in blocks if rock.x > b.x and rock.y == b.y]
        # print(f'Blocking blocks for {rock} = {blocking_blocks}')
        # print(f'Checking for rock {rock}')
        if len(blocking_blocks) > 0:
            blocking_blocks.sort(key=lambda b: b.x, reverse=True)
            max_x = blocking_blocks[0].x
            # print(f'Max x: {max_x}')

            blocking_rocks = [r for r in rocks if rock.x > r.x > max_x and rock.y == r.y]
            # print(f'Blocking rocks after block for {rock} = {blocking_rocks}')

            if len(blocking_rocks) > 0:
                # move to lowest rock
                max_x = 0
                blocking_rocks.sort(key=lambda r: r.x, reverse=True)
                # print(f'blocking rocks for rock {rock} after max_x {max_x}: {blocking_rocks}')
                max_x = blocking_rocks[0].x
            # print(f'Lowest block is at y {max_y}')
            rock.x = max_x + 1
        else:
            blocking_rocks = [r for r in rocks if rock.x > r.x and rock.y == r.y]
            # print(f'Blocking rocks for {rock} = {blocking_rocks}')

            if len(blocking_rocks) == 0:
                # move to lowest y
                rock.x = 0
            else:
                # move to lowest rock
                blocking_rocks.sort(key=lambda r: r.x, reverse=True)
                max_x = blocking_rocks[0].x
                # print(f'Lowest rock is at y {max_y}')
                rock.x = max_x + 1


def move_south(rocks: list[Rock], blocks: list[Block], y_limit: int):
    rocks.reverse()
    for rock in rocks:
        # print()
        # print(f'Checking rock {rock}')
        blocking_blocks = [b for b in blocks if rock.y < b.y and rock.x == b.x]
        # print(f'Blocking blocks for {rock} = {blocking_blocks}, limit {y_limit}')
        if len(blocking_blocks) > 0:
            blocking_blocks.sort(key=lambda b: b.y)
            max_y = blocking_blocks[0].y

            blocking_rocks = [r for r in rocks if rock.y < r.y < max_y and rock.x == r.x]
            if len(blocking_rocks) > 0:
                # print(f'Blocking rocks after block for {rock} = {blocking_rocks}')
                blocking_rocks.sort(key=lambda b: b.y)
                max_y = blocking_rocks[0].y
            # print(f'Highest block is at y {max_y}')
            rock.y = max_y - 1
        else:
            blocking_rocks = [r for r in rocks if rock.y < r.y and rock.x == r.x]
            # print(f'Blocking rocks for {rock} = {blocking_rocks}')

            if len(blocking_rocks) == 0:
                # move to lowest y
                rock.y = y_limit - 1
            else:
                # move to lowest rock
                blocking_rocks.sort(key=lambda b: b.y)
                # print(f'blocking rocks above current {rock} = {blocking_rocks}')
                max_y = blocking_rocks[0].y
                # print(f'Highest rock is at y {max_y}')
                rock.y = max_y - 1


def move_east(rocks: list[Rock], blocks: list[Block], x_limit: int):
    rocks.sort(key=lambda r: r.x, reverse=True)
    for rock in rocks:
        # print()
        blocking_blocks = [b for b in blocks if rock.x < b.x and rock.y == b.y]
        # print(f'Blocking blocks for {rock} = {blocking_blocks}')
        if len(blocking_blocks) > 0:
            blocking_blocks.sort(key=lambda b: b.x)
            max_x = blocking_blocks[0].x

            blocking_rocks = [r for r in rocks if rock.x < r.x < max_x and rock.y == r.y]
            # print(f'Blocking rocks after block for {rock} = {blocking_rocks}')

            if len(blocking_rocks) > 0:
                # move to lowest rock
                max_x = 0
                blocking_rocks.sort(key=lambda b: b.x)
                max_x = blocking_rocks[0].x
            # print(f'Lowest block is at y {max_y}')
            rock.x = max_x - 1
        else:
            blocking_rocks = [r for r in rocks if rock.x < r.x and rock.y == r.y]
            # print(f'Blocking rocks for {rock} = {blocking_rocks}')

            if len(blocking_rocks) == 0:
                # move to lowest y
                rock.x = x_limit - 1
            else:
                # move to lowest rock
                blocking_rocks.sort(key=lambda b: b.x)
                max_x = blocking_rocks[0].x
                # print(f'Lowest rock is at y {max_y}')
                rock.x = max_x - 1


def print_to_file(rocks: list[Rock], blocks: list[Block], x_limit: int, y_limit: int):
    with open("14/output.txt", "a") as f:
        for y in range(0, y_limit, 1):
            line = ''
            for x in range(0, x_limit, 1):
                pos_rocks = [r for r in rocks if r.x == x and r.y == y]
                pos_blocks = [b for b in blocks if b.x == x and b.y == y]
                if len(pos_rocks) == 0 and len(pos_blocks) == 0:
                    line += '.'
                else:
                    if len(pos_rocks) == 1:
                        line += 'O'
                    elif len(pos_rocks) > 1:
                        print(f'Too many rocks at {x, y}: {pos_rocks}')
                    if len(pos_blocks) == 1:
                        line += '#'
                    elif len(pos_blocks) > 1:
                        print(f'Too many blocks at {x, y}: {[pos_blocks]}')

            print(f'{line}', file=f)
        print('', file=f)
