# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


def find_hidden_word(mat, word):

    wordlen = len(word)
    row_len = len(mat)
    col_len = len(mat[0])

    # find position which match the first alphabet of the word
    pivots = [(i, j) for i, row in enumerate(mat) for j, col in enumerate(row) if col == word[0]]

    if not pivots:
        print("Couldn't find the word!")
        return 0

    results = []

    # can be further factor the code to make it shorter!
    for point in pivots:
        row, col = point
        up = ''.join(mat[row-i][col] for i in range(wordlen) if row-i>=0)
        if up == word:
            results.append((point, 'up'))

        dn = ''.join(mat[row+i][col] for i in range(wordlen) if row+i<row_len)
        if dn == word:
            results.append((point, 'down'))

        ll = ''.join(mat[row][col-i] for i in range(wordlen) if col-i>=0)
        if ll == word:
            results.append((point, 'left'))

        rr = ''.join(mat[row][col+i] for i in range(wordlen) if col+i<col_len)
        if rr == word:
            results.append((point, 'right'))

        ur = ''.join(mat[row-i][col+i] for i in range(wordlen) if row-i>=0 and col+i<col_len)
        if ur == word:
            results.append((point, 'up-right'))

        dr = ''.join(mat[row+i][col+i] for i in range(wordlen) if row+i<row_len and col+i<col_len)
        if dr == word:
            results.append((point, 'down-right'))

        ul = ''.join(mat[row-i][col-i] for i in range(wordlen) if row-i>=0 and col-i>=0)
        if ul == word:
            results.append((point, 'up-left'))

        dl = ''.join(mat[row+i][col-i] for i in range(wordlen) if row+i<row_len and col-i>=0)
        if dl == word:
            results.append((point, 'down-left'))

    if results:
        for result in results:
            point, direction = result
            print(f'position: {point}, direction: {direction}')
    else:
        print("Couldn't find the word!")
        return 0


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'N', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]

    find_hidden_word(matrix, 'ASS')
    find_hidden_word(matrix, 'FOAM')
    find_hidden_word(matrix, 'SON')
