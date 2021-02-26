from collections import namedtuple

Firma = namedtuple("Firma", "name position year")


def put_data(file_name, staff):  # staff is an arr with staff structures
    with open(f"files/{file_name}.txt", "w") as file:
        for worker in staff:
            file.write(f'{worker.name}, {worker.position}, {worker.year}\n')


def get_arr_data(file_name):
    with open(f'files/{file_name}.txt', 'r') as file:
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
    """ Insert sort """
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1].name > staff[i].name:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff

# def sort_data(staff):
#     """ Bubble sort """
#     for _ in range(1, len(staff)):
#         for i in range(len(staff)-1):
#             if staff[i].name > staff[i+1].name:
#                 staff[i], staff[i+1] = staff[i+1], staff[i]
#
#     return staff

# def sort_data(staff):
#     """ Choice sort """
#     for current in range(len(staff)-1):
#         for following in range(current + 1, len(staff)):
#             if staff[following].name < staff[current].name:
#                 staff[following], staff[current] = staff[current], staff[following]
#
#     return staff


def get_staff_with_experience(exp, staff):
    from datetime import datetime as date

    have_exp = [worker.name for worker in staff if date.now().year - worker.year > exp]

    if len(have_exp) != 0:
        print(f'The existed staff with {exp} year experience:')
        print(*have_exp, sep='\n')
    else:
        print(f'No person has {exp} year experience')
