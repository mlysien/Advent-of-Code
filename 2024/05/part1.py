from operator import indexOf

import numpy as np

def parse_ordering_rules(rules_page):
    rules = {}
    for line in rules_page:
        items = []
        key =  int(line.split('|')[0])
        value = int(line.split('|')[1])

        if key in rules:
            items = rules[key]

        items.append(value)
        rules[key] = items

    return rules

def parse_updates(updates_page):
    items = []
    for line in updates_page:
        items.append([int(i) for i in line.split(',')])

    return items

def check_update(update_line, rules: {}):

    for i in range(0, len(update_line)):
        current_item = update_line[i]

        if current_item in rules:
            update_line_rules = rules[current_item]

            for rule in update_line_rules:
                if rule in update_line:
                    if update_line.index(rule) >= i:
                        continue
                    else:
                        return False

    return True


with open('puzzle.txt', 'r+') as puzzle:
    result = 0
    data = puzzle.read().split('\n\n')
    rules_page = [x for x in data[0].split('\n')]
    updates_page = [x for x in data[1].split('\n')]

    # parse ordering rules from file
    ordering_rules = parse_ordering_rules(rules_page)

    # parse updates from file
    updates = parse_updates(updates_page)

    # check updates
    for update in updates:
        if check_update(update, ordering_rules):
            middle = len(update) // 2
            result += update[middle]

    print(f'Result: {result}')