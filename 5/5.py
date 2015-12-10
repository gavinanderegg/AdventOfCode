nice = 0

lines = [line.rstrip() for line in open('input')]

for line in lines:
    naughty = False

    if len(re.findall('(.*?[aeiou])', line)) < 3:
        continue

    if len(re.findall('(.)\1{1,}', line)) < 1:
        continue