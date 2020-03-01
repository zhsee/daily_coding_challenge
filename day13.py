# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def extract_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return set(substrings)

def longest_k_distinct_char_substring(s, k):
    k_substrings = (ss for ss in extract_all_substrings(s) if len(set(ss)) == k)
    return max(map(len, k_substrings))

print(longest_k_distinct_char_substring('abcba', 2))
print(longest_k_distinct_char_substring('abceabb', 2))

