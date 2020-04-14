# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

def is_palindrome(s):
    return s == s[::-1]


def longest_palindrome_substring(s):
    str_len = len(s)

    max_len = 0
    lgs = None

    for i in range(1, str_len):
        j = 1
        if len(s[i + 1:]) * 2 + 1 < max_len:      # stop when remaining median unable to form lgs > current lgs
            break
        while i - j >= 0 and i + j + 1 <= str_len:
            lgs_candidate = s[i-j:i+j+1]
            new_len = len(lgs_candidate)
            if new_len > max_len and is_palindrome(lgs_candidate):
                lgs = lgs_candidate
                max_len = new_len
            j += 1
    return lgs

print(longest_palindrome_substring("bcdcb"))
print(longest_palindrome_substring("bananas"))
print(longest_palindrome_substring("sananas"))
print(longest_palindrome_substring("abc"))
