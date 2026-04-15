class BSTNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        # your code here, helper functions are encouraged
        ...

    def find(self, key):
        # your code here, helper functions are encouraged
        ...

    def update(self, key, data):
        # your code here, helper functions are encouraged
        ...

    def count_odd_elements(self): ...
