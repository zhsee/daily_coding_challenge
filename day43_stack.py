# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.


class Stack():
    def __init__(self):
        self.stack = []
        # self.maximum = None

    def push(self, val):
        self.stack.append(val)
        # if not self.maximum or val > self.maximum:
        #     self.maximum = val

    def pop(self):
        return None if len(self.stack) == 0 else self.stack.pop()

    def max(self):
        return None if len(self.stack) == 0 else max(self.stack)

    def __str__(self):
        return ', '.join(map(str, self.stack))


mystack = Stack()
mystack.push(9)
mystack.push(6)
mystack.push(8)
print(mystack)
print(mystack.max())
aa = mystack.pop()
print(aa)
print(mystack.max())
