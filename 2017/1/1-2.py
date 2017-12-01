lines = [line.rstrip() for line in open('input')]

circ_sum = 0

for line in lines:
    double_line = line + line

    for pos in xrange(0, len(line)):
        half_pos = (len(line) / 2) + pos

        if double_line[pos] == double_line[half_pos]:
            circ_sum += int(double_line[pos])

print circ_sum
