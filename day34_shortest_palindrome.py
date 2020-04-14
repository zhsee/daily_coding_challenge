# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

def minlenpalindrome(s):
    rev_s = s[::-1]
    length = len(s)

    if length == 1:
        return s

    match_idx = 0
    for i in range(length):
        if s[:i] == rev_s[length-i:]:
            match_idx = length - i

    return rev_s[:match_idx] + s


print(minlenpalindrome('google'))
print(minlenpalindrome('race'))
print(minlenpalindrome('a'))
print(minlenpalindrome('geeks')) ; # no working with this algorithm! answer should be gskeeksg.

def min_insertion_recursive(s, l, h):
    if l > h:
        return 9999
    elif l == h:
        return 0
    elif l == h - 1:
        if s[l] == s[h]:
            return 0
        else:
            return 1

    if s[l] == s[h]:
        return min_insertion_recursive(s, l + 1, h - 1)
    else:
        return min(min_insertion_recursive(s, l, h - 1),
                   min_insertion_recursive(s, l + 1, h)) + 1


print(min_insertion_recursive('geeks', 0, len('geeks')-1))

