file = file('input', 'r')

floor = 0

char = file.read(1)

while len(char) > 0:
    if len(char.strip()) > 0:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    char = file.read(1)

print floor
