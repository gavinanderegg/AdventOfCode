total = 0

lines = [line.rstrip() for line in open('input')]

for line in lines:
    dims = line.split('x')

    dim_info = {
        'width': {
            'x': int(dims[0]),
            'y': int(dims[1]),
        },
        'height': {
            'x': int(dims[1]),
            'y': int(dims[2]),
        },
        'depth': {
            'x': int(dims[0]),
            'y': int(dims[2]),
        },
    }

    width_val = int(dims[0]) * int(dims[1])
    height_val = int(dims[1]) * int(dims[2])
    depth_val = int(dims[0]) * int(dims[2])

    smallest = {
        'name': 'width',
        'val': width_val,
    }

    if height_val < smallest['val']:
        smallest = {
            'name': 'height',
            'val': height_val,
        }

    if depth_val < smallest['val']:
        smallest = {
            'name': 'depth',
            'val': depth_val,
        }

    ribbon = (dim_info[smallest['name']]['x'] * 2) + (dim_info[smallest['name']]['y'] * 2)

    bow = int(dims[0]) * int(dims[1]) * int(dims[2])

    total += ribbon + bow

print total
