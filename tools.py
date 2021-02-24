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
