class FixedSizeArray:
    def __init__(self, cap):
        self.li = []
        self.cap = cap


class DASimple:
    def __init__(self):  # Do not change the constructor (use as is)
        self.len = 0
        self.cap = 4
        self.a = FixedSizeArray(self.cap)

    def double_cap(self):  # Doubles the array’s capacity (Call it as needed!)
        self.cap = 2 * self.cap
        a = FixedSizeArray(self.cap)
        for i in range(self.len):
            a[i] = self.a[i]
        self.a = a

    def is_empty(self):  # Returns True if array empty, otherwise False
        ...
    def prepend(self, e: object):  # Put e as first item in array
        ...
    def reverse(self):  # Reverses array elements in place (no new list/arr)
        ...
