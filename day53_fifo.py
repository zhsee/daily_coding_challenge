# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, val):
        self.stack1.append(val)


    def dequeue(self):
        if not self.stack1:
            return None

        if len(self.stack1) == 1:
            return self.stack1.pop()

        while (self.stack1):
            self.stack2.append(self.stack1.pop())
        ret_val = self.stack2.pop()

        while (self.stack2):
            self.stack1.append(self.stack2.pop())

        return ret_val


    def __str__(self):
        if self.stack1:
            return f"{', '.join(map(str, self.stack1))}"
        else:
            return 'empty'

if __name__ == '__main__':
    q = Queue()
    q.enqueue('1')
    print(q)
    q.enqueue('2')
    print(q)
    q.enqueue('3')
    print(q)

    print('dequeueing...')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)


