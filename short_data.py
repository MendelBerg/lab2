import tools


f = open('files/data.txt', 'r')
count = sum(1 for _ in open('files/data.txt', 'r'))

workers_data = []

for x in range(count):
    name, position, year = f.readline().split(', ')
    workers_data.append(tools.Firma(name, position, int(year.replace('\n', ''))))

tools.sort_data(workers_data)


new_file = open("files/data_shorted.txt", "w")

for x in workers_data:
    new_file.write(f'{x.name}, {x.position}, {x.year}\n')

new_file.close()
