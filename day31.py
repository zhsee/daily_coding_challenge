# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

# print 2d array
def print2d(array):
    maxwidth = max(len(str(array[i][j])) for i in range(len(array)) for j in range(len(array[0])))
    for row in array:
        for col in row:
            print(f'{str(col):{maxwidth + 1}}', end="")
        print()
    print()

#edit distance from str1 -> str2
def edit_distance(str1, str2):
    # build a 2d array
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # dp = [[0] * (n + 1)] * (m + 1)

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1],     # insert ←
                    dp[i-1][j-1],   # repalce ↖
                    dp[i-1][j],     # remove ↑
                )
    print2d(dp)
    return dp[m][n]


# print2d([[1, 2, 3, 4, 5], [12, 456, 4, 6, 3]])
edit_distance('kitten', 'sitting')
edit_distance('ros', 'horse')
edit_distance('horse', 'ros')

