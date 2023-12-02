import re

lines = [line.rstrip() for line in open('1.txt')]

sum = 0

for line in lines:
    first = re.search('\d', line)[0]
    last = re.search('\d', line[::-1])[0]

    sum += int(first + last)

print(sum)


