import re

lines = [line.rstrip() for line in open('1.txt')]

# This is gross, but I was tooling around for too long with
# a regex pattern that was melting my brain… I want to just
# move on to today's problem.
numbers = {
    'one': 1, '1': 1,
    'two': 2, '2': 2,
    'three': 3, '3': 3,
    'four': 4, '4': 4,
    'five': 5, '5': 5,
    'six': 6, '6': 6,
    'seven': 7, '7': 7,
    'eight': 8, '8': 8,
    'nine': 9, '9': 9,
}

sum = 0

for line in lines:
    number_words = list(numbers.keys())

    first = 0
    last = 0

    partial = ''

    for char in line:
        partial += char

        for word in number_words:
            if word in partial:
                first = word
                break

        if first != 0:
            break

    first = numbers[first]

    partial = ''
    rev_line = line[::-1]

    for char in rev_line:
        partial = char + partial

        for word in number_words:
            if word in partial:
                last = word
                break

        if last != 0:
            break

    last = numbers[last]

    sum += int(str(first) + str(last))

print(sum)


