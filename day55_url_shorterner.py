# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?


def id2shorturl(id):
    mapping = 'abcdefghijklmnopqrxtuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ0123456789'
    url = ''

    while(id > 0):
        url += mapping[id%62]
        id = id//62

    return url[::-1]


def shorturl2id(url):
    id = 0
    for cc in url:
        cc_ord = ord(cc)
        if cc_ord >= ord('a') and cc_ord <= ord('z'):
            id = id*62 + cc_ord - ord('a')
        elif cc_ord >= ord('A') and cc_ord <= ord('Z'):
            id = id*62 + cc_ord - ord('A') + 26
        elif cc_ord >= ord('0') and cc_ord <= ord('9'):
            id = id*62 + cc_ord - ord('0') + 52
        else:
            print('Error!')
            return

    return id


print(id2shorturl(3874))
print(shorturl2id('baE'))
