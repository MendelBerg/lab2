class Firma:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year


def sort_data(lst):
    for bubble in range(1, len(lst)):
        for struct in range(len(lst) - 1):
            if lst[struct].name > lst[struct + 1].name:
                lst[struct], lst[struct + 1] = lst[struct + 1], lst[struct]


f = open('files/data.txt', 'r')
count = sum(1 for _ in open('files/data.txt', 'r'))

workers_data = []

for x in range(count):
    name, position, year = f.readline().split(', ')
    workers_data.append(Firma(name, position, int(year.replace('\n', ''))))

sort_data(workers_data)


new_file = open("files/data_shorted.txt", "w")

for x in workers_data:
    new_file.write(f'{x.name}, {x.position}, {x.year}\n')

new_file.close()
