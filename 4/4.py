import md5

key = 'pqrstuv'

complete = False
count = 0

while not complete:
    m = md5.new()
    m.update(key + str(count))
    hash_val = m.hexdigest()

    if hash_val[:5] == '00000':
        print hash_val
        print count
        complete = True

    count += 1
