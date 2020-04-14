
class LinkList():
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            self.head = Node(data=nodes.pop(0))
            node = self.head
            for ele in nodes:
                node.next = Node(data=ele)
                node = node.next


    def __repr__(self):
        repr_ = [self.head.data]
        node = self.head
        while node.next:
            repr_.append(node.next.data)
            node = node.next
        return '->'.join(map(str, repr_))


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self):
        return self.data


if __name__ == '__main__':
    llist = LinkList([1,3,5,7])
    print(llist)

    for ele in llist:
        print(ele)
