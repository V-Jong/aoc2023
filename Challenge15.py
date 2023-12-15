def do_challenge():
    file = open('15/input.txt', 'r')
    lines = file.read().splitlines()

    value = 0
    for char in lines[0].split(','):
        m = 0
        for c in char:
            m = (m + ord(c)) * 17 % 256
        value += m

        print(f'ascii for {char} = {m}')
    print(f'Total: {value}')
