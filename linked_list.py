from node import Node

class LinkedList:
    def remove(self, node):
        if self.head is None:
            return
        if node.val == self.head.val:
            node.set_next(None)
            self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while curr is not None:
                if node.val == curr.val:
                    prev.set_next(curr.next)
                    curr.set_next(None)
                    return
                prev = curr
                curr = curr.next


    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(f"({node.val[0]}, {node.val[1]})")
        return " -> ".join(nodes)