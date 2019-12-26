import sys

line_string = open('input').read().strip()

# split the read file into a list of ints
init_data = list(map(int, line_string.split(',')))
data = init_data.copy()
max_address = len(data) - 1

# For the first version of this, I was able to get away with reading in
# input in groups of four, but that was a hack.

pc = 0    # program counter

while pc <= max_address:
    inst = data[pc]

    if inst == 1:    # addition
        arg_1 = data[pc + 1]
        arg_2 = data[pc + 2]
        res_addr = data[pc + 3]

        pc += 4

        try:
            data[res_addr] = data[arg_1] + data[arg_2]
        except:
            sys.exit('Error: Couldn\'t address while adding')

    elif inst == 2:    # multiplication
        arg_1 = data[pc + 1]
        arg_2 = data[pc + 2]
        res_addr = data[pc + 3]

        pc += 4

        try:
            data[res_addr] = data[arg_1] * data[arg_2]
        except:
            sys.exit('Error: Couldn\'t address while multiplying')

    elif inst == 99:
        # halt
        break

    else:
        sys.exit('Error: Unknown opcode found at pc ' + str(pc) + ' : ' + str(inst))

print('Data at [0]: ' + str(data[0]))
