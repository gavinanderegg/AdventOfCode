lines = [line.rstrip() for line in open('input')]

repeat_sum = 0

for line in lines:
    for pos in xrange(0, len(line)):
        if pos == len(line) - 1:
            if line[pos] == line[0]:
                repeat_sum += int(line[pos])
        else:
            if line[pos] == line[pos + 1]:
                repeat_sum += int(line[pos])

print repeat_sum
