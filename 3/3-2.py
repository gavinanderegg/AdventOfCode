map_hash = {
    '0.0': 1,
}

santa_location = {
    'x': 0,
    'y': 0,
}

robo_location = {
    'x': 0,
    'y': 0,
}

turn = 1

file = file('input', 'r')
char = file.read(1)

while len(char) > 0:
    if len(char.strip()) > 0:
        if char == '^':
            if turn % 2 == 0:
                robo_location['y'] += 1
            else:
                santa_location['y'] += 1
        elif char == '>':
            if turn % 2 == 0:
                robo_location['x'] += 1
            else:
                santa_location['x'] += 1
        elif char == 'v':
            if turn % 2 == 0:
                robo_location['y'] -= 1
            else:
                santa_location['y'] -= 1
        elif char == '<':
            if turn % 2 == 0:
                robo_location['x'] -= 1
            else:
                santa_location['x'] -= 1

        turn += 1

        if turn % 2 == 0:
            location_string = str(robo_location['x']) + '.' + str(robo_location['y'])
        else:
            location_string = str(santa_location['x']) + '.' + str(santa_location['y'])

        if location_string in map_hash.keys():
            map_hash[location_string] += 1
        else:
            map_hash[location_string] = 1

        char = file.read(1)

print len(map_hash)