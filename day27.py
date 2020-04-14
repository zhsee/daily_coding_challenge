# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


def brackets_checker(s):
    l_brackets = ('(', '[', '{')
    r_brackets = (')', ']', '}')
    bracket_pairs = dict(zip(r_brackets, l_brackets))
    all_brackets = l_brackets + r_brackets

    bracket_stack = []
    for c in s:
        if c in l_brackets:
            bracket_stack.append(c)
        elif c in r_brackets:
            if not bracket_stack or bracket_stack.pop() != bracket_pairs[c]:
                return False

    return False if bracket_stack else True

assert brackets_checker("([])[]({})") == True
assert brackets_checker("]are you crazy()") == False
assert brackets_checker("are you crazy(") == False
assert brackets_checker("([)]") == False
assert brackets_checker("((()") == False
