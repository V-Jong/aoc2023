import itertools
import sys
from math import gcd


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.key} | left: {self.left} | right: {self.right}'

    def __repr__(self):
        return f'{self.key} | left: {self.left} | right: {self.right}'


def do_challenge():
    file = open('8/input.txt', 'r')
    lines = file.readlines()
    instructions = [*lines[0].strip()]
    node_lines = lines[2:]
    nodes = {}
    # print(f'Instructions: {instructions}')
    for node_line in node_lines:
        node_parts = node_line.split('=')
        node_key = node_parts[0].strip()
        node_refs = node_parts[1].strip().split(',')
        nodes.update({node_key: Node(node_key, node_refs[0].strip()[1:], node_refs[1].strip()[:-1])})
    # print(f'Nodes: {nodes} {len(nodes)}')
    start_nodes = []
    for node in nodes.values():
        if node.key[-1] == 'A':
            start_nodes.append(node)
    # start_node = nodes.get('FQA')
    # steps = calc_steps(nodes, start_node, instructions)
    # print(f'Steps: {steps}')
    steps = []
    for start_node in start_nodes:
        steps_node = calc_steps(nodes, start_node, instructions)
        print(f'Steps for start {start_node} = {steps_node}')
        steps.append(steps_node)
    lcm = 1
    for i in steps:
        lcm = lcm * i // gcd(lcm, i)
    print(f'LCM is {lcm}')


def calc_steps(nodes: dict, current_node: Node, instructions: list[str]):
    steps = 0
    current_instructions = instructions.copy()
    while current_node.key[-1] != 'Z':
        if len(current_instructions) == 0:
            current_instructions = instructions.copy()
        nav_to = current_instructions[0]
        current_instructions.remove(nav_to)
        steps += 1
        current_node = nodes.get(current_node.left if nav_to == 'L' else current_node.right)
    return steps
