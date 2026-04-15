class Node:
    def __init__(self, prev, item, next):
        self.prev = prev
        self.item = item
        self.next = next


class DoubleLinkedList:
    def __init__(self):  # Implement as you see fit.
        ...
    def front(self) -> object:
        # Return the front element in a non-empty list, otherwise raise exception.
        if self.is_empty():
            raise Exception("front on an empty list")

    def insert_after_front(self, item: object):
        # Insert a new element after the front element in a non-empty list,
        # or raise an exception if the list is empty. Returns nothing.
        ...
