from functools import cache

@cache
def calculate(current_stone, iterations) -> int:
    if iterations == 0:
        return 1
    # if the stone is engraved with the number 0 it is replaced by a stone engraved with the number 1
    if current_stone == 0:
        return calculate(1, iterations - 1)

    if len(str(current_stone)) % 2 == 0:
        size = len(str(current_stone)) // 2
        stone_one = int(''.join([i for i in str(current_stone)[:size]]))
        stone_two = int(''.join([i for i in str(current_stone)[size:]]))

        return calculate(stone_one, iterations - 1) + calculate(stone_two, iterations - 1)

    return calculate(current_stone * 2024, iterations - 1)

with open('puzzle.txt', 'r') as puzzle:
    stones = [int(s) for s in puzzle.read().split()]
    result = 0 

    for stone in stones:
        result +=  calculate(stone, 75)

    print(f'Result: {result}')