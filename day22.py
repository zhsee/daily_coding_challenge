# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

# bruteforce
def string2sentence(s, ws):
    answer = []
    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            if s[i:j] in ws:
                answer.append(s[i:j])
    return ' '.join(answer)


# recursive:
def wordbreak(s, ws):
    if len(s) == 0:
        return ''
    for i in range(1, len(s) + 1):
        if s[:i] in ws:
            return s[:i] + ' ' + wordbreak(s[i:], ws)

print(string2sentence('thequickbrownfox', ['the', 'quick', 'brown', 'fox']))
print(wordbreak('thequickbrownfox', ['the', 'quick', 'brown', 'fox']))
