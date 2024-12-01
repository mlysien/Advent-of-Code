def read_almanac() -> list[str]:
    file = open("puzzle.txt", "r")
    return file.read().split('\n\n')


class Seed:
    def __init__(self, value: int, mapped: bool):
        self.value = value
        self.mapped = mapped


almanac = read_almanac()
seeds = []
mapping = {}
for line_number, line in enumerate(almanac):
    if line_number == 0:
        seeds = [Seed(int(x), mapped=False) for x in line.split(':')[1].strip().split(' ')]
    else:
        map = [n for n in line.split(':')[1].split('\n') if n]

        for seed in seeds:
            seed.mapped = False

        for m in map:
            destination_range_start = int(m.split(' ')[0])
            source_range_start = int(m.split(' ')[1])
            range_length = int(m.split(' ')[2])

            for i, seed in enumerate(seeds):
                if not seed.mapped and source_range_start <= seed.value <= (source_range_start + range_length - 1):
                    calc = seed.value - source_range_start
                    seeds[i].value = destination_range_start + calc
                    seeds[i].mapped = True

print(f'Lowest seed location number: {min([s.value for s in seeds])}')
