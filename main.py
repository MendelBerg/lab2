import tools

tools.put_data('data', [
    tools.Firma(
        input(f'The person #{_+1}\nName: '),
        input('Position: '),
        int(input('Year: '))
    )
    for _ in range(
        int(input('Amount structures: '))
    )
])
