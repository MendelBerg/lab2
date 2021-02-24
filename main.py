import tools

tools.put_data('data', [
    tools.Firma(
        input('Name: '),
        input('Position: '),
        int(input('Year: '))
    )
    for _ in range(
        int(input('Amount structures: '))
    )
])
