import tools

f = open('files/data_shorted.txt', 'r')
count = sum(1 for _ in open('files/data_shorted.txt', 'r'))

workers_data = []

for x in range(count):
    name, position, year = f.readline().split(', ')
    workers_data.append(tools.Firma(name, position, int(year.replace('\n', ''))))

experience = int(input('Minimally experience: '))
tools.have_experience(experience, workers_data)
