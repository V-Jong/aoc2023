import re

file = open('19/input.txt', 'r')
lines = file.read().splitlines()


def do_challenge():
    empty_line = [i for i, l in enumerate(lines) if l == ''][0]

    workflows = lines[0:empty_line]
    ratings = lines[empty_line + 1:]

    workflows_p = {}
    ratings_p = []

    # Register workflows
    for workflow in workflows:
        workflow_reg = re.findall('[a-z]+{', workflow)[0]
        rules_reg = re.findall('{.+}', workflow)[0]
        workflow_key = workflow_reg[0:-1]
        rule_lines = rules_reg[1:-1]
        rules_split = rule_lines.split(',')
        rules = []
        for rule_split in rules_split:
            # print(f'Checking rule {rule_split}')
            if ':' in rule_split:
                # print(f'Rule contains :')
                if '<' in rule_split:
                    # print(f'Rule contains <')
                    rules.append(get_rule(rule_split, '<'))
                if '>' in rule_split:
                    # print(f'Rule contains >')
                    rules.append(get_rule(rule_split, '>'))
            else:
                rules.append(Rule('', '', -1, rule_split))

        n_workflow = Workflow(workflow_key, rules)
        workflows_p.update({workflow_key: n_workflow})
        # print(f'Added workflow: {n_workflow}')

    # Register ratings
    for rating in ratings:
        rating = rating[1:-1]
        rating_split = rating.split(',')
        r_dict = {}
        for r_split in rating_split:
            r2_split = r_split.split('=')
            variable = r2_split[0]
            value = int(r2_split[1])
            r_dict.update({variable: value})
        ratings_p.append(r_dict)

    initial_workflow = workflows_p.get('in')
    accepted = []
    for rating_dict in ratings_p:
        workflow_stack = [initial_workflow]

        while workflow_stack:
            current_wf = workflow_stack.pop()
            print(f'\nChecking workflow "{current_wf.key}"')
            rule_index = 0
            rule_stack = [current_wf.rules[rule_index]]

            while rule_stack:
                current_rule = rule_stack.pop()
                print(f'\nChecking rule: {current_rule}')
                dest_tmp = current_rule.destination

                if current_rule.has_comparison():
                    variable_val = rating_dict.get(current_rule.variable)
                    print(f'Rule has comparison, {current_rule.variable} = {variable_val}')
                    if current_rule.within_limit(variable_val):
                        if dest_tmp == 'A':
                            print(f'Dest is A, stopping')
                            accepted.append(rating_dict)
                            break
                        if dest_tmp == 'R':
                            print(f'Dest is R, stopping')
                            break
                        print(f'Val {variable_val} within limit, adding to workflow stack: {current_rule.destination}')
                        workflow_stack.append(workflows_p.get(current_rule.destination))
                    else:
                        rule_index += 1
                        print(
                            f'Val {variable_val} not within limit, checking next rule: {current_wf.rules[rule_index]}')
                        rule_stack.append(current_wf.rules[rule_index])
                else:
                    if dest_tmp == 'A':
                        print(f'Dest is A, stopping')
                        accepted.append(rating_dict)
                        break
                    if dest_tmp == 'R':
                        print(f'Dest is R, stopping')
                        break
                    print(f'Current rule has no comparison, going to workflow {current_rule.destination}')
                    workflow_stack.append(workflows_p.get(current_rule.destination))

    print(f'Accepted ratings: {accepted}')
    total = 0
    for acc in accepted:
        for val in acc.values():
            total += val
    print(f'Total rating: {total}')


def get_rule(line: str, comparator: str):
    # print(f'Getting rule from {line} using comparator {comparator}')
    variable_split = line.split(comparator)
    # print(f'rule split {variable_split}')
    variable = variable_split[0]
    limit_dest_split = variable_split[1]
    limit_split = limit_dest_split.split(':')
    limit = int(limit_split[0])
    dest = limit_split[1]
    return Rule(variable, comparator, limit, dest)


class Workflow:
    def __init__(self, key, rules):
        self.key = key
        self.rules = rules

    def __str__(self):
        return f'Workflow: {self.key}, rules: {self.rules}'

    def __repr__(self):
        return f'Workflow: {self.key}, rules: {self.rules}'


class Rule:
    def __init__(self, variable, comparator, limit, destination):
        self.variable = variable
        self.comparator = comparator
        self.limit = limit
        self.destination = destination

    def within_limit(self, value):
        if self.comparator == '>':
            return value > self.limit
        elif self.comparator == '<':
            return value < self.limit
        return False

    def has_comparison(self):
        return self.limit != -1

    def __str__(self):
        return f'if: {self.variable} {self.comparator} {self.limit}, then {self.destination}'

    def __repr__(self):
        return f'if: {self.variable} {self.comparator} {self.limit}, then {self.destination}'
