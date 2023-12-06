import itertools
import re


class Map:
    def __init__(self, source, target, range):
        self.source = source
        self.target = target
        self.range = range

    def __str__(self):
        return f'Map: {self.source}, {self.target}, {self.range}'

    def __repr__(self):
        return f'Map: {self.source}, {self.target}, {self.range}'


def do_challenge():
    do_challenge_a()


def do_challenge_a():
    file = open('5/input.txt', 'r')
    lines = file.readlines()
    lines = list(map(lambda l: l.replace('\n', ''), lines))
    key_seed_to_soil = 'seed-to-soil map:'
    key_soil_to_fert = 'soil-to-fertilizer map:'
    key_fert_to_water = 'fertilizer-to-water map:'
    key_water_to_light = 'water-to-light map:'
    key_light_to_temp = 'light-to-temperature map:'
    key_temp_to_humid = 'temperature-to-humidity map:'
    key_humid_to_loc = 'humidity-to-location map:'

    total_points = 0
    with open("5/output.txt", "a") as f:
        # For part a:
        # seeds = list(map(int, re.findall(r'\d+', lines[0])))

        idx_seed_to_soil = 0
        idx_soil_to_fert = 0
        idx_fert_to_water = 0
        idx_water_to_light = 0
        idx_light_to_temp = 0
        idx_temp_to_humid = 0
        idx_humid_to_loc = 0

        for line_index, line in enumerate(lines):
            if line == key_seed_to_soil:
                idx_seed_to_soil = line_index
            if line == key_soil_to_fert:
                idx_soil_to_fert = line_index
            if line == key_fert_to_water:
                idx_fert_to_water = line_index
            if line == key_water_to_light:
                idx_water_to_light = line_index
            if line == key_light_to_temp:
                idx_light_to_temp = line_index
            if line == key_temp_to_humid:
                idx_temp_to_humid = line_index
            if line == key_humid_to_loc:
                idx_humid_to_loc = line_index
        seed_to_soil = list(map(lambda m: create_map_from_line(m), lines[idx_seed_to_soil + 1: idx_soil_to_fert - 1]))
        soil_to_fert = list(map(lambda m: create_map_from_line(m), lines[idx_soil_to_fert + 1: idx_fert_to_water - 1]))
        fert_to_water = list(map(lambda m: create_map_from_line(m), lines[idx_fert_to_water + 1: idx_water_to_light - 1]))
        water_to_light = list(map(lambda m: create_map_from_line(m), lines[idx_water_to_light + 1: idx_light_to_temp - 1]))
        light_to_temp = list(map(lambda m: create_map_from_line(m), lines[idx_light_to_temp + 1: idx_temp_to_humid - 1]))
        temp_to_humid = list(map(lambda m: create_map_from_line(m), lines[idx_temp_to_humid + 1: idx_humid_to_loc - 1]))
        humid_to_loc = list(map(lambda m: create_map_from_line(m), lines[idx_humid_to_loc + 1: len(lines)]))

        # print(f'Seeds ({len(seeds)}) {seeds}')

        targets = []
        # For part a:
        # for seed in seeds:
        #     dest_seed_to_soil = calculate_seed_destination(seed, seed_to_soil)
        #     # print(f'seed {seed} has dest_seed_to_soil {dest_seed_to_soil}')
        #
        #     dest_soil_to_fert = calculate_seed_destination(dest_seed_to_soil, soil_to_fert)
        #     # print(f'seed {seed} has dest_soil_to_fert {dest_soil_to_fert}')
        #
        #     dest_fert_to_water = calculate_seed_destination(dest_soil_to_fert, fert_to_water)
        #     # print(f'seed {seed} has dest_fert_to_water {dest_fert_to_water}')
        #
        #     dest_water_to_light = calculate_seed_destination(dest_fert_to_water, water_to_light)
        #     # print(f'seed {seed} has dest_water_to_light {dest_water_to_light}')
        #
        #     dest_light_to_temp = calculate_seed_destination(dest_water_to_light, light_to_temp)
        #     # print(f'seed {seed} has dest_light_to_temp {dest_light_to_temp}')
        #
        #     dest_temp_to_humid = calculate_seed_destination(dest_light_to_temp, temp_to_humid)
        #     # print(f'seed {seed} has dest_temp_to_humid {dest_temp_to_humid}')
        #
        #     dest_humid_to_loc = calculate_seed_destination(dest_temp_to_humid, humid_to_loc)
        #     print(f'seed {seed} has dest_humid_to_loc {dest_humid_to_loc}')
        #
        #     targets.append(dest_humid_to_loc)
        # seeds = []

        # For part b:
        seeds_start = list(map(int, re.findall(r'\d+', lines[0])))
        seed_batches = list(divide_list_in_batches(seeds_start, 2))

        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(8)

        lowest = pool.starmap(get_lowest_for_seed_range, zip(seed_batches, itertools.repeat(seed_to_soil),
                                                               itertools.repeat(soil_to_fert),
                                                               itertools.repeat(fert_to_water),
                                                               itertools.repeat(water_to_light),
                                                               itertools.repeat(light_to_temp),
                                                               itertools.repeat(temp_to_humid),
                                                               itertools.repeat(humid_to_loc)))
        # print(f'Split {split_seeds}')
        # for seed_batch in seed_batches:
            # get_lowest_for_seed_range(seed_batch, seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc)
            # seeds.extend(range(start, start + steps))

        # print(f'Locs: {targets}')
        print(f'Lowest: {min(lowest)}')
        # print(f'Min: {min(targets)}')


def do_challenge_b():
    print()


def create_map_from_line(line: str):
    numbers = list(map(int, re.findall(r'\d+', line)))
    return Map(numbers[1], numbers[0], numbers[2])


def calculate_seed_destination(seed: int, maps: list[Map]):
    relevant_map = 0
    for c_map in maps:
        start = c_map.source
        end = c_map.source + c_map.range - 1
        if start <= seed <= end:
            relevant_map = c_map
    if relevant_map == 0:
        # print(f'Seed {seed} not in map, returning seed')
        return seed

    # print(f'Checking dest for seed {seed} with map {relevant_map}')
    steps = seed - relevant_map.source
    # print(f'Seed {seed} in map, calculating dest')
    return relevant_map.target + steps


def divide_list_in_batches(list_to_split, batch_size):
    for i in range(0, len(list_to_split), batch_size):
        yield list_to_split[i:i + batch_size]


def get_lowest_for_seed_range(seed_batch: list[int], seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_loc):
    lowest = -1
    start = seed_batch[0]
    steps = seed_batch[1]
    stop = start + steps - 1
    print(f'Min seed {start}, max seed {stop}')
    current = start
    while current <= stop:
        dest_seed_to_soil = calculate_seed_destination(current, seed_to_soil)
        # print(f'seed {seed} has dest_seed_to_soil {dest_seed_to_soil}')

        dest_soil_to_fert = calculate_seed_destination(dest_seed_to_soil, soil_to_fert)
        # print(f'seed {seed} has dest_soil_to_fert {dest_soil_to_fert}')

        dest_fert_to_water = calculate_seed_destination(dest_soil_to_fert, fert_to_water)
        # print(f'seed {seed} has dest_fert_to_water {dest_fert_to_water}')

        dest_water_to_light = calculate_seed_destination(dest_fert_to_water, water_to_light)
        # print(f'seed {seed} has dest_water_to_light {dest_water_to_light}')

        dest_light_to_temp = calculate_seed_destination(dest_water_to_light, light_to_temp)
        # print(f'seed {seed} has dest_light_to_temp {dest_light_to_temp}')

        dest_temp_to_humid = calculate_seed_destination(dest_light_to_temp, temp_to_humid)
        # print(f'seed {seed} has dest_temp_to_humid {dest_temp_to_humid}')

        dest_humid_to_loc = calculate_seed_destination(dest_temp_to_humid, humid_to_loc)
        print(f'seed {current} has dest_humid_to_loc {dest_humid_to_loc}')

        if lowest == -1:
            lowest = dest_humid_to_loc
        else:
            lowest = dest_humid_to_loc if dest_humid_to_loc < lowest else lowest

        current += 1
    return lowest
