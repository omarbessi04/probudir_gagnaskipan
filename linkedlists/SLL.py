class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class SingleLinkedList:
    def __init__(self):  # Do not change the constructor (use as is)
        self._len = 0
        self._head = None  # The implementation only has a head reference (no tail)

    def front(self):  # Return first elem in non-empty list, otherwise exception
        # The time complexity of this methods is: O(1)
        if self.is_empty():
            raise Exception("front on empty list")
        return self._head.item

    def push_front(self, item):  # Insert an element at the front of the list.
        # The time complexity of this methods is: O(1)
        node = Node(item, self._head)  # Create a new node with item and next.
        self._head = node
        self._len += 1

    def back(self):  # Return last elem in list if non-empty, otherwise exception.
        # The time complexity of this methods is: __???___
        ...

    def push_back(self, item):  # Insert an element at the back of the list
        # The time complexity of this methods is: __???____
        ...
