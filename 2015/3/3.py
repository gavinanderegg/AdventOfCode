file = file('input', 'r')

map_hash = {
    '0.0': 1,
}
location = {
    'x': 0,
    'y': 0,
}

char = file.read(1)

while len(char) > 0:
    if len(char.strip()) > 0:
        if char == '^':
            location['y'] += 1
        elif char == '>':
            location['x'] += 1
        elif char == 'v':
            location['y'] -= 1
        elif char == '<':
            location['x'] -= 1

        location_string = str(location['x']) + '.' + str(location['y'])

        if location_string  in map_hash.keys():
            map_hash[location_string] += 1
        else:
            map_hash[location_string] = 1

        char = file.read(1)

print len(map_hash)