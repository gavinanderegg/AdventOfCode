import md5
import pdb

key = 'ffykfhsq'

complete = False
count = 0
chars = 0

realPassword = {}

while not complete:
    m = md5.new()
    m.update(key + str(count))
    hash_val = m.hexdigest()

    if hash_val[:5] == '00000':
        print "Char: " + hash_val[6:7] + "  " + hash_val[5:6] + " " + str(realPassword)

        if int(hash_val[5:6], 16) in [0, 1, 2, 3, 4, 5, 6, 7]:
            if not realPassword.get(hash_val[5:6]):
                realPassword[hash_val[5:6]] = hash_val[6:7]

        if len(realPassword) == 8:
            print hash_val
            complete = True

    count += 1

for key in sorted(realPassword.iterkeys()):
    print "%s: %s" % (key, realPassword[key])


# 757573c9
