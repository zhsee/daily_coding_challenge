# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

import itertools

alphabet = 'abcdefghijklmnopqrxtuvwxyz'
encode_map = {aa: str(idx) for idx, aa in enumerate(alphabet, start=1)}

def get_key_from_val(mydict, value):
    for k, v in mydict.items():
        if v == value:
            return k
    else:
        return None


def multiSlice(s,cutpoints):
    k = len(cutpoints)
    if k == 0:
        return [s]
    else:
        multislices = [s[:cutpoints[0]]]
        multislices.extend(s[cutpoints[i]:cutpoints[i+1]] for i in range(k-1))
        multislices.append(s[cutpoints[k-1]:])
        return multislices


def allPartitions(s):
    n = len(s)
    cuts = list(range(1,n))
    for k in range(n):
        for cutpoints in itertools.combinations(cuts,k):
            print(f'DEBUG k: {k} cutpoints: {cutpoints}')
            yield multiSlice(s,cutpoints)


def decoding(s):
    valid_decoded_combinations = []
    for aa in allPartitions(s):
        if all(map(lambda x: True if int(x) > 0 and int(x) <= 26 else False, aa)):
            valid_decoded_combinations.append(aa)

    decoded_results = [''.join(map(lambda x: get_key_from_val(encode_map, x), combi)) for combi in valid_decoded_combinations]
    return (len(valid_decoded_combinations), decoded_results)

# print(decoding('111'))
# print(decoding('1263'))

for aa in allPartitions('World'):
    print(aa)
