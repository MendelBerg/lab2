from collections import namedtuple

Firma = namedtuple("Firma", "name position year")


def put_data(file_name, staff):
    file = open(f"files/{file_name}.txt", "w")

    for worker in staff:
        file.write(f'{worker.name}, {worker.position}, {worker.year}\n')

    file.close()


def get_arr_data(file_name):
    file = open(f'files/{file_name}.txt', 'r')

    return [
        Firma(
            name=worker[0],
            position=worker[1],
            year=int(worker[2].replace('\n', ''))
        )
        for worker in [
            file.readline().split(', ')
            for _ in range(
                sum(1 for _ in open(f'files/{file_name}.txt', 'r'))
            )
        ]
    ]


def sort_data(staff):
    for _ in range(1, len(staff)):
        for i in range(len(staff) - 1):
            if staff[i].name > staff[i + 1].name:
                staff[i], staff[i + 1] = staff[i + 1], staff[i]

    return staff


def get_staff_with_experience(exp, staff):
    from datetime import datetime as date

    have_exp = [worker.name for worker in staff if date.now().year - worker.year > exp]

    if len(have_exp) != 0:
        print(f'The existed staff with {exp} year experience:')
        print(*have_exp, sep='\n')
    else:
        print(f'No person has {exp} year experience')
