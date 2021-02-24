from datetime import datetime as date


class Firma:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year


def have_experience(exp, staff):
    staff_true = [person.name for person in staff if date.now().year - person.year > exp]

    if len(staff_true) != 0:
        print(f'The existed staff with {exp} year experience:')
        print(*staff_true, sep='\n')
    else:
        print(f'No person has {exp} year experience')


f = open('files/data_shorted.txt', 'r')
count = sum(1 for _ in open('files/data_shorted.txt', 'r'))

workers_data = []

for x in range(count):
    name, position, year = f.readline().split(', ')
    workers_data.append(Firma(name, position, int(year.replace('\n', ''))))

experience = int(input('Minimally experience: '))
have_experience(experience, workers_data)
