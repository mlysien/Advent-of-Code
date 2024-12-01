def read_almanac() -> list[str]:
    file = open("puzzle.txt", "r")
    return file.read().split('\n\n')


class Seed:
    def __init__(self, start: int, end: int):
        self.seed_start = start
        self.seed_end = end


class Map:
    def __init__(self, name: str, section: []):
        self.name = name
        self.section = section

    def __str__(self):
        return f'Map {self.name}'


plants = []
maps = []
# read seeds and map
for line_index, line in enumerate(read_almanac()):
    if line_index == 0:
        data = line.split(':')[1].strip().split(' ')
        for i in range(len(data)):
            if i % 2 == 0:
                plants.append(Seed(int(data[i]), int(data[i]) + int(data[i + 1]) - 1))
    else:
        name = line.split(':')[0].strip()
        sections = [n for n in line.split(':')[1].split('\n') if n]
        maps.append(Map(name, sections))

min_location = 999999999999999999999999
for i, plant in enumerate(plants):
    print(f'Plant {i+1} from {len(plants)}')
    for seed in range(plant.seed_start, plant.seed_end):
        for map in maps:
            mapped = {}
            for section in map.section:
                destination_start = int(section.split(' ')[0])
                source_start = int(section.split(' ')[1])
                step = int(section.split(' ')[2])

                if source_start <= seed <= (source_start + step - 1):
                    calc = seed - source_start
                    value = destination_start + calc

                    if value not in mapped and seed not in mapped:
                        seed = value
                        mapped[seed] = True
        if seed < min_location:
            min_location = seed

print(f'Lowest location number: {min_location}')
