file = file('input', 'r')

floor = 0
pos = 1
reached_basement = False

char = file.read(1)

while len(char) > 0:
    if len(char.strip()) > 0:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    if floor < 0 and reached_basement == False:
        print "First entered the basement at: ",  pos
        reached_basement = True

    pos += 1

    char = file.read(1)

print floor
