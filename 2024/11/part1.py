with open('puzzle.txt', 'r') as puzzle:
    stones = [int(s) for s in puzzle.read().split()]
    counter = 0

    while counter < 25:
        print(f'Counter: {counter}...')
        buffer = list()
        for index, stone in enumerate(stones):
            # if the stone is engraved with the number 0
            if stone == 0:
                # it is replaced by a stone engraved with the number 1.
                buffer.append(1)
                continue

            # if the stone is engraved with a number that has an even number of digits.
            if len(str(stone)) % 2 == 0:
                # it is replaced by two stones, e.g. 253000 -> 253 000
                size = len(str(stone)) // 2
                stone_one = int(''.join([i for i in str(stone)[:size]]))
                stone_two = int(''.join([i for i in str(stone)[size:]]))
                buffer.extend([stone_one, stone_two])
                continue
            # if none of the other rules apply, the stone is replaced by a new stone;
            # the old stone's number multiplied by 2024
            buffer.append(stones[index] * 2024)

        stones = buffer.copy()
        counter += 1

    print(f'Result: {len(stones)}')