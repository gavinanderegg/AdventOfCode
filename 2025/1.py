import re

lines = [line.rstrip() for line in open('1.txt')]

hits = 0
angle = 50

for line in lines:
    expression = '([RL]{1})(\d+)'
    direction = re.search(expression, line)[1]
    amount = int(re.search(expression, line)[2])

    if direction == 'L':
        angle -= amount
    elif direction == 'R':
        angle += amount

    angle = abs(angle % 100)

    if angle == 0:
        hits += 1

print(hits)


