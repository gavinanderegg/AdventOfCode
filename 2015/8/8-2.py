import re
import codecs

line_total = 0
encoded_total = 0

lines = [line.rstrip() for line in open('input')]

for line in lines:
    line_length = len(line)

    encoded = codecs.encode(line, 'unicode_escape')
    encoded = encoded.replace('"', '/"') # \ gets stripped.
    encoded = '"' + encoded + '"'

    encoded_length = len(encoded)

    print line, ' ', encoded, ' ', line_length, ' ', encoded_length

    line_total += line_length
    encoded_total += encoded_length


print '\n\n'
print 'Line Total: ', line_total
print 'Encoded Total: ', encoded_total

print encoded_total - line_total