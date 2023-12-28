class Jar:
    def __init__(self, capacity=12, n=0):
        self.capacity = capacity
        self.size = n

    def __str__(self):
        cookie = ""
        for _ in range(self.size):
            cookie += "🍪"
        return cookie

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("capacity is less than 0")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > int(self.capacity):
            raise ValueError("more than capacity")
        if n < 0:
            raise ValueError("no more cookies")
        self._size = n
        return n


