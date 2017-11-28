import md5

key = 'ffykfhsq'

complete = False
count = 0
chars = 0

while not complete:
    m = md5.new()
    m.update(key + str(count))
    hash_val = m.hexdigest()

    if hash_val[:5] == '00000':
        print hash_val[5:6]

        chars += 1

        if chars == 8:
            complete = True

    count += 1
