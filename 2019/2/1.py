import sys

line_string = open('q1_input').read().strip()

# split the read file into a list of ints
data = list(map(int, line_string.split(',')))

# if len(data) % 4 != 0:
#     sys.exit('Error: Instruction count not divisible by 4')

instructions = []
current_items = []

# put the data into 4-int arrays to work from
for count, item in enumerate(data):
    current_items.append(item)

    if (count + 1) % 4 == 0:
        instructions.append(current_items)
        current_items = []

for inst in instructions:
    if inst[0] == 1:
        # addition
        try:
            data[inst[3]] = data[inst[1]] + data[inst[2]]
        except:
            sys.exit('Error: Couldn\'t address while adding')

    elif inst[0] == 2:
        # multiplication
        try:
            data[inst[3]] = data[inst[1]] * data[inst[2]]
        except:
            sys.exit('Error: Couldn\'t address while multiplying')

    elif inst[0] == 99:
        # halt
        break

    else:
        sys.exit('Error: Unknown opcode found')

print('Data at [0]: ' + str(data[0]))
