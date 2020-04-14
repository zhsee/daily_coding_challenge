# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

import re

def string_splitter(s, k):
    if len(s) < k:
        return [s]
    if any(map(lambda x: len(x) > k, s.split())):
        return None
    space_index = [aa.start(0) for aa in re.finditer(r'\s', s) if aa.start(0) <= k]
    split_index = space_index[-1]
    return [s[:split_index]] + string_splitter(s[split_index+1:], k)

if __name__ == "__main__":
    string = 'the quick brown fox jumps over the lazy dog'
    print(string_splitter(string, 10))
    string = 'she sells seashell on the seashore'
    print(string_splitter(string, 10))
