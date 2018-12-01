import datetime

print(datetime.datetime.now())

answer = 0
freqs = [0]
notfound = True

lines = open('input.txt').read().split('\n')

while notfound:
    for line in lines:
        answer += int(line.strip())

        if answer in freqs:
            print(answer)

            print(datetime.datetime.now())

            notfound = False

            break

        freqs.append(answer)

