import re
import codecs

str_total = 0
code_total = 0

lines = [line.rstrip() for line in open('input')]

for line in lines:
    code_length = len(line)

    unquoted = line[:-1][1:]
    escaped = codecs.decode(unquoted, 'unicode_escape')

    str_length = len(escaped)

    print line, ' ', code_length, ' ', str_length

    str_total += str_length
    code_total += code_length


print '\n\n'
print 'String Total: ', str_total
print 'Code Total: ', code_total

print code_total - str_total