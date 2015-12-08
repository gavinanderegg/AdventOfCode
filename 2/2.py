total = 0

lines = [line.rstrip() for line in open('input')]

for line in lines:
    smallest_side = 0
    width = 0
    height = 0
    depth = 0

    dims = line.split('x')

    width = int(dims[0]) * int(dims[1])
    smallest_side = width

    height = int(dims[0]) * int(dims[2])
    if height < smallest_side:
        smallest_side = height

    depth = int(dims[1]) * int(dims[2])
    if depth <  smallest_side:
        smallest_side = depth

    total += (2 * width) + (2 * height) + (2 * depth) + smallest_side

print total
