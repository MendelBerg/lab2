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

    return staff_true if len(staff_true) > 0 else f'No person has {exp} year experience'


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

experience = int(input('Minimally experience: '))
exist_exp = have_experience(experience, data)

# ===========================================================
new_file = open("data_2.txt", "w")

for x in data:
    new_file.write(f'{x.name}, {x.position}, {x.year}\n')

if type(exist_exp) is str:
    new_file.write('\n' + exist_exp)
else:
    new_file.write(f'\nThe existed staff with {experience} year experience: \n')
    for name in exist_exp:
        new_file.write(f'{name}\n')

new_file.close()

new_file = open("data_2.txt", "r")
print(new_file.read())
