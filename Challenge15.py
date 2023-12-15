def do_challenge():
    file = open('15/input.txt', 'r')
    lines = file.read().splitlines()

    value = 0
    room = {}
    for i in range(0, 256, 1):
        room.update({i: []})
    for char in lines[0].split(','):
        box_nr = 0
        if '=' in char:
            c_split = char.split('=')
            label = c_split[0]
            operation = '='
            focal = c_split[1]
        else:
            label = char.split('-')[0]
            operation = '-'
            focal = -1
        print(f'Found label {label}')
        for c in label:
            box_nr = (box_nr + ord(c)) * 17 % 256

        box_list = room.get(box_nr)
        label_index = -1
        for b_index, box_item in enumerate(box_list):
            if box_item[0] == label:
                label_index = b_index
                break
        if operation == '=':
            new_lens = (label, focal)
            if label_index == -1:
                box_list.append(new_lens)
            else:
                box_list[label_index] = new_lens
        elif operation == '-':
            if label_index != -1:
                del box_list[label_index]
                print(f'List after removing {label_index}: {box_list}')

        print(f'ascii for {label} = {box_nr}')

    for box_nr, box_list in room.items():
        if len(box_list) > 0:
            for box_index, box_item in enumerate(box_list):
                print(f'Add box index {box_index} with item {box_item}')
                value += (1 + box_nr) * (box_index + 1) * (int(box_item[1]))
    print(f'Total: {value}')
