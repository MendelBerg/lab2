import tools

amount = int(input('Amount structures: '))
workers_data = []

for x in range(amount):
    print(f'The person №{x + 1}')
    workers_data.append(tools.Firma(
        input('Name: '),
        input('Position: '),
        int(input('Year: '))
    ))

tools.put_data('data', workers_data)
