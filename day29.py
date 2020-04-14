# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

import re

def encode(s):
    split = [aa.group() for aa in re.finditer(r'(.)\1+|.', s)]
    return ''.join((str(len(aa))+aa[0]) for aa in split)

def decode(s):
    pairs = (s[i:i+2] for i in range(0, len(s), 2))
    return ''.join((pair[1]*int(pair[0]) for pair in pairs))


print(encode('AAAABBBCCDAA'))
print(decode('4A3B2C1D2A'))
