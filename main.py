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
    staff_true = [person.name for person in staff if 2021 - int(person.year) > exp]

    if type(staff_true) is list:
        print(f'The existed staff with {exp} year experience:')
        print(*staff_true)
    else:
        print(f'No person has {exp} year experience')


# ===========================================================
amount = int(input('Amount structures: '))
arr = []

for x in range(amount):
    print(f'The person №{x + 1}')
    name = input('Name: ')
    position = input('Position: ')
    year = int(input('Year: '))
    arr.append(Firma(name, position, year))

file = open("data.txt", "w")

for x in arr:
    file.write(f'{x.name}, {x.position}, {x.year}\n')

file.close()

# ===========================================================
f = open('data.txt', 'r')
count = sum(1 for x in open('data.txt', 'r'))

a = [f.readline() for _ in range(count)]
data = []

for x in a:
    name, position, year = x.split(', ')
    data.append(Firma(name, position, year.replace('\n', '')))

# ===========================================================
sort_data(data)

new_file = open("data_2.txt", "w")

for x in data:
    new_file.write(f'{x.name}, {x.position}, {x.year}\n')

new_file.close()

new_file = open("data_2.txt", "r")
print(new_file.read())

# =====================================================

experience = int(input('Minimally experience: '))
have_experience(experience, data)