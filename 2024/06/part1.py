def get_starting_point(array):
    for r, row in enumerate(array):
        for c, val in enumerate(row):
            if val == "^":
                return r, c

with open('puzzle.txt', "r") as file:
    map = list(map(list, map(str.strip, file.readlines())))

    rows = len(map)
    columns = len(map[0])

    x, y = get_starting_point(map)
    dx, dy = -1, 0
    visited = set()

    while True:
        visited.add((x, y))
        if not (0 <= x + dx < rows and 0 <= y + dy < columns):
            break
        if map[x + dx][y + dy] == "#":
            dy, dx = -dx, dy
        else:
            x += dx
            y += dy

    print(f"Result: {len(visited)}")
