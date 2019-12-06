import re

lines = [line.rstrip() for line in open('input')]
completed_lines = []

wires = {}


assign_number_regex = '^(\d+) -> ([a-z]+)$' # 123 -> x
assign_value_regex = '^([a-z]+) -> ([a-z]+)$' # lx -> a
and_regex = '^([a-z]+) AND ([a-z]+) -> ([a-z]+)$' # x AND y -> d
or_regex = '^([a-z]+) OR ([a-z]+) -> ([a-z]+)$' # x OR y -> e
lshift_regex = '^([a-z]+) LSHIFT (\d+) -> ([a-z]+)$' # x LSHIFT 2 -> f
rshift_regex = '^([a-z]+) RSHIFT (\d+) -> ([a-z]+)$' # y RSHIFT 2 -> g
not_regex = '^NOT ([a-z]+) -> ([a-z]+)$' # NOT y -> i
one_and_regex = '^1 AND ([a-z]+) -> ([a-z]+)$' # 1 AND lu -> lv


while len(completed_lines) < len(lines):
    print(str(len(completed_lines)) + ' of ' + str(len(lines)) + ' completed')


    for line in lines:
        if line in completed_lines:
            continue


        if re.search(assign_number_regex, line):
            m = re.search(assign_number_regex, line)

            wires[m.group(2)] = int(m.group(1))
            completed_lines.append(line)


        if re.search(assign_value_regex, line):
            m = re.search(assign_value_regex, line)

            if m.group(1) in wires:
                wires[m.group(2)] = wires[m.group(1)]
                completed_lines.append(line)


        elif re.search(and_regex, line):
            m = re.search(and_regex, line)

            if m.group(1) in wires and m.group(2) in wires:
                wires[m.group(3)] = int(wires[m.group(1)]) & int(wires[m.group(2)])
                completed_lines.append(line)


        elif re.search(or_regex, line):
            m = re.search(or_regex, line)

            if m.group(1) in wires and m.group(2) in wires:
                wires[m.group(3)] = int(wires[m.group(1)]) | int(wires[m.group(2)])
                completed_lines.append(line)


        elif re.search(lshift_regex, line):
            m = re.search(lshift_regex, line)

            if m.group(1) in wires:
                wires[m.group(3)] = int(wires[m.group(1)]) << int(m.group(2))
                completed_lines.append(line)


        elif re.search(rshift_regex, line):
            m = re.search(rshift_regex, line)

            if m.group(1) in wires:
                wires[m.group(3)] = int(wires[m.group(1)]) >> int(m.group(2))
                completed_lines.append(line)


        elif re.search(not_regex, line):
            m = re.search(not_regex, line)

            if m.group(1) in wires:
                wires[m.group(2)] = int(wires[m.group(1)]) ^ 0b1111111111111111
                completed_lines.append(line)


        elif re.search(one_and_regex, line):
            m = re.search(one_and_regex, line)

            if m.group(1) in wires:
                wires[m.group(2)] = 1 & int(wires[m.group(1)])
                completed_lines.append(line)



print(wires)