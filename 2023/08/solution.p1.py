def read_puzzle():
    file = open("puzzle.txt", "r")
    directions = [0 if d == "L" else 1 for d in file.readline()[:-1]]

    # read empty line
    file.readline()

    nodes = {}
    for line in file.readlines():
        nodes[line.split(" = ")[0]] = (line.split("(")[1].split(",")[0], line.split(", ")[1].split(")")[0])

    return directions, nodes


steps = 0
current_node = "AAA"
directions, nodes = read_puzzle()

while current_node != "ZZZ":
    for direction in directions:
        steps += 1
        current_node = nodes[current_node][direction]
        if current_node == "ZZZ":
            break

print(steps)
