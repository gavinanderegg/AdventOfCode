answer = 0

with open('input.txt') as txt:
    lines = txt.readlines()

    for line in lines:
        answer += int(line.strip())

print(answer)