def get_disk_blocks(map: str) -> [int]:
    file_id = 0
    disk_blocks = []

    for element in range(0, len(map)):
        if element % 2 == 0:
            for j in range(0, int(map[element])):
                disk_blocks.append(file_id)
            file_id += 1
        else:
            for j in range(0, int(map[element])):
                disk_blocks.append(-1)

    return disk_blocks


with open('puzzle.txt', 'r') as puzzle:
    disk_map = puzzle.readline().strip()
    checksum = 0
    blocks = get_disk_blocks(disk_map)
    free_space_indexes = [index for index, value in enumerate(blocks) if value == -1]
    free_space_iterator = 0

    while True:
        while blocks[-1] == -1:
            blocks.pop()

        free_space_index = free_space_indexes[free_space_iterator]

        if free_space_index >= len(blocks):
            break

        blocks[free_space_index] = blocks.pop()
        free_space_iterator += 1

    for i in range(0, len(blocks)):
        checksum += i * blocks[i]

    print(f'Checksum: {checksum}')