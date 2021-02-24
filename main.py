class Firma:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year


amount = int(input('Amount structures: '))
workers_data = []

for x in range(amount):
    print(f'The person №{x + 1}')
    name = input('Name: ')
    position = input('Position: ')
    year = int(input('Year: '))
    workers_data.append(Firma(name, position, year))

file = open("files/data.txt", "w")

for x in workers_data:
    file.write(f'{x.name}, {x.position}, {x.year}\n')

file.close()
