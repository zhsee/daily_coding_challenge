# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).


class node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def evalBT(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        # print(f'{type(root.value)} {root.value}')
        return int(root.value)

    valLeft = evalBT(root.left)
    valRight = evalBT(root.right)

    if root.value == '+':
        return valLeft + valRight
    elif root.value == '-':
        return valLeft - valRight
    elif root.value == '*':
        return valLeft * valRight
    elif root.value == '/':
        return valLeft / valRight
    else:
        print('unknown operation!')
        return None

if __name__ == '__main__':
    root = node('*')
    root.left = node('+')
    root.right = node('+')
    root.left.left = node(3)
    root.left.right = node(2)
    root.right.left = node(4)
    root.right.right = node(5)

    print(evalBT(root))

    root0 = node('+')
    root0.left = node('*')
    root0.left.left = node('5')
    root0.left.right = node('4')
    root0.right = node('-')
    root0.right.left = node('100')
    root0.right.right = node('20')
    print(evalBT(root0))


    root1 = node('+')
    root1.left = node('*')
    root1.left.left = node('5')
    root1.left.right = node('4')
    root1.right = node('-')
    root1.right.left = node('100')
    root1.right.right = node('/')
    root1.right.right.left = node('20')
    root1.right.right.right = node('2')

    print(evalBT(root1))
