# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

import re

def autocomplete(s, ss):
    result = [a for a in ss if re.search(fr'^{s}', a)]
    # result = [a for a in ss if a.startswith(s)]
    return result

print(autocomplete('de', ['dog', 'deer', 'deal']))

# This is an unoptimized answer.  I will explore better solution next time.
