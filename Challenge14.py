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
    for line_index, line in enumerate(lines):
        chars = [*line]
        for c_index, char in enumerate(chars):
            if char == 'O':
                rocks.append(Rock(c_index, line_index))
            if char == '#':
                blocks.append(Block(c_index, line_index))

    max_points = len(lines)
    # move_north(rocks, blocks)
    # print(f'Blocks after moving north')
    # to do: 1000000000
    do_cycle(1, rocks, blocks, len(lines))
    rocks.sort(key=lambda r: r.x)
    sum_points = 0
    for rock in rocks:
        print(f'{rock}, points: {max_points - rock.y}')
        sum_points += max_points - rock.y

    print(f'Sum: {sum_points}')


def do_cycle(times: int, rocks: list[Rock], blocks: list[Block], y_limit: int):
    for i in range(0, times, 1):
        # move_north(rocks, blocks)
        # move_west(rocks, blocks)
        move_south(rocks, blocks, y_limit)
        # move_east(rocks, blocks)


def move_north(rocks: list[Rock], blocks: list[Block]):
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


def move_south(rocks: list[Rock], blocks: list[Block], y_limit: int):
    rocks.reverse()
    for rock in rocks:
        print()
        blocking_blocks = [b for b in blocks if rock.y < b.y and rock.x == b.x]
        print(f'Blocking blocks for {rock} = {blocking_blocks}, limit {y_limit}')
        if len(blocking_blocks) > 0:
            blocking_blocks.sort(key=lambda b: b.y)
            max_y = blocking_blocks[0].y

            blocking_rocks = [r for r in rocks if r.y > rock.y and rock.x == r.x]
            if len(blocking_rocks) > 0:
                print(f'Blocking rocks after block for {rock} = {blocking_rocks}')
                blocking_rocks.sort(key=lambda b: b.y)
                max_y = blocking_rocks[0].y
            print(f'Highest block is at y {max_y}')
            rock.y = max_y - 1
        else:
            blocking_rocks = [r for r in rocks if rock.y < r.y and rock.x == r.x]
            print(f'Blocking rocks for {rock} = {blocking_rocks}')

            if len(blocking_rocks) == 0:
                # move to lowest y
                rock.y = y_limit
            else:
                # move to lowest rock
                blocking_rocks.sort(key=lambda b: b.y, reverse=True)
                max_y = blocking_rocks[0].y
                print(f'Highest rock is at y {max_y}')
                rock.y = max_y - 1


def move_east(rocks: list[Rock], blocks: list[Block]):
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
