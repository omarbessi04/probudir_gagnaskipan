class Bucket:
    ...
    # insert(key,data)
    # contains(key)
    # find(key)
    # remove(key)
    # update(key, data)
    # __setitem__(key, data)
    # __getitem__(key)


class HashMap:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.bucket_arr = [None] * self.capacity
        for i in range(self.capacity):
            self.bucket_arr[i] = Bucket()

    def remove(self, key): ...

    def contains(self, key): ...

    def find(self, key): ...
