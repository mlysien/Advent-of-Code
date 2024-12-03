﻿import re

def mul(x, y):
    return x * y

with open('puzzle.txt') as file:
    memory = file.read()
    instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', memory)
    result = 0
    can_execute = True

    for instruction in instructions:
        if instruction == 'don\'t()':
            can_execute = False
            continue

        if instruction == 'do()':
            can_execute = True
            continue

        if can_execute:
            digits = [int(s) for s in re.findall(r'\b\d+\b', instruction)]
            result += mul(digits[0], digits[1])

    print(f'Result: {result}')