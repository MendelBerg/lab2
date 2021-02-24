from datetime import datetime as date


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


def have_experience(exp, staff):
    staff_true = [person.name for person in staff if date.now().year - person.year > exp]

    if len(staff_true) != 0:
        print(f'The existed staff with {exp} year experience:')
        print(*staff_true, sep='\n')
    else:
        print(f'No person has {exp} year experience')


def get_arr_data(file_name):
    count = sum(1 for _ in open(f'files/{file_name}.txt', 'r'))
    f = open(f'files/{file_name}.txt', 'r')

    workers_data = []

    for x in range(count):
        name, position, year = f.readline().split(', ')
        workers_data.append(Firma(name, position, int(year.replace('\n', ''))))

    return workers_data


def put_data(file_name, arr_data):
    file = open(f"files/{file_name}.txt", "w")

    for struct in arr_data:
        file.write(f'{struct.name}, {struct.position}, {struct.year}\n')

    file.close()
